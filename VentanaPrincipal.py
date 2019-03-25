import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from sqlite3 import dbapi2
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

class VentanaPrincipal(Gtk.Window):




    def __init__(self):
        Gtk.Window.__init__(self, title="Inmobiliaria")

        # Nos conectamos a la base
        self.bbdd = dbapi2.connect("BasesDeDatos/Casas.db")

        #self.bbdd.execute("create table Casas(codc number, dir text,habitaciones number, superficie number)")


        """
        cursor=self.bbdd.cursor()
        self.bbdd.cursor().execute("insert into Casas Values(1, 'dir 1', 1, 70)")
        cursor = self.bbdd.cursor()
        self.bbdd.cursor().execute("insert into Casas Values(2, 'dir 2', 2, 80)")
        cursor = self.bbdd.cursor()
        self.bbdd.cursor().execute("insert into Casas Values(3, 'dir 3', 3, 90)")
        self.bbdd.commit()
        """
        self.informeCasas()
        casas = self.bbdd.cursor().execute("select codc,dir,habitaciones,superficie from Casas")

        self.mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.comprar = Gtk.Button("Comprar")
        self.comprar.connect("clicked", self.compra)

        self.modelo = Gtk.ListStore(int, str, int, int)

        # Rellenamos el modelo
        for x in casas:
            self.modelo.append([x[0], x[1], x[2], x[3]])

        # Creamos la tabla
        self.tabla = Gtk.TreeView()

        celdaText = Gtk.CellRendererText()
        columnaCodigo = Gtk.TreeViewColumn('Codigo', celdaText, text=0)
        self.tabla.append_column(columnaCodigo)

        celdaText2 = Gtk.CellRendererText(xalign=1)
        columnaNombre = Gtk.TreeViewColumn('direccion', celdaText2, text=1)
        self.tabla.append_column(columnaNombre)

        celdaText3 = Gtk.CellRendererText(xalign=1)
        columnaPrecio = Gtk.TreeViewColumn('habitaciones', celdaText3, text=2)
        self.tabla.append_column(columnaPrecio)

        celdaText3 = Gtk.CellRendererText(xalign=1)
        columnaPrecio = Gtk.TreeViewColumn('superficie', celdaText3, text=2)
        self.tabla.append_column(columnaPrecio)

        self.tabla.set_model(self.modelo)

        seleccion = self.tabla.get_selection()
        seleccion.connect("changed", self.seleccion)

        self.mainBox.pack_start(self.tabla, True, True, 0)
        self.mainBox.pack_start(self.comprar, False, False, 0)

        self.add(self.mainBox)
        self.show_all()

    def seleccion(self,seleccion):
        """Funcion que sobrescribe un array dependiendo de la seleccion del usuario"""
        vista, puntero = seleccion.get_selected()
        if puntero is not None:
            codigo=self.modelo[puntero][0]
            dir=self.modelo[puntero][1]
            hab=self.modelo[puntero][2]
            sup=self.modelo[puntero][3]

            self.casa=[codigo,dir,hab,sup]
            print(self.casa)

    def compra(self,boton):
        print("compra")
        #genera una factura con la casa seleccionada en el treeview
        guion = []
        doc = SimpleDocTemplate("Ejemplo.pdf", pagesize=A4, showBoundary=0)

        estilo = getSampleStyleSheet()
        cabecera = estilo['Heading4']

        tabla = Table(self.casa, colWidths=80, rowHeights=30)

        tabla.setStyle(TableStyle([
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.blue),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.green),
            ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.grey)

        ]))

        parrafo = Paragraph("Gracias por su compra", estilo)

        guion.append(tabla)
        guion.append(parrafo)
        doc.build(guion)

    def informeCasas(self):
        #informe con todas las casas a la venta
        print("x")
        doc = SimpleDocTemplate("ListaCasas.pdf", pagesize=A4)
        guion = []
        casas=self.bbdd.cursor().execute("select codc,dir,habitaciones,superficie from Casas")
        print("casas"+str(casas))
        listaCasas=list()
        for casa in casas:
            listaCasas.append(list(casa))

        tabla = Table(listaCasas, colWidths=80, rowHeights=30)
        tabla.setStyle(TableStyle([

            ('BOX', (0, 0), (-1, 0), 1, colors.black),

            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]))
        guion.append(tabla)

        doc.build(guion)
