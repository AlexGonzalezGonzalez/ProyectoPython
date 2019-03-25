import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from sqlite3 import dbapi2
from ProyectoInmobiliaria.BasesDeDatos.FuncionesDB import FuncionesDB

class VentanaRegistro(Gtk.Window):

    def __init__(self):
        print("Iniciando la Ventana Login")

        # Conexion a la base
        self.bbdd = dbapi2.connect("BasesDeDatos/Usuarios.db")

        # Iniciamos la ventana
        Gtk.Window.__init__(self, title="Registro")

        # Box que contiene todo
        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.fc=FuncionesDB()

        boxH1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        boxH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=72)
        boxFin = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=65)


        # Componentes y caracteristicas de la ventana
        lblUser = Gtk.Label("Usuario")
        self.txtUser = Gtk.Entry()

        lblPass = Gtk.Label("Contraseña")
        self.txtPass = Gtk.Entry()
        self.txtPass.set_visibility(False)

        lblCombo=Gtk.Label("Role")
        self.comboRole = Gtk.ComboBoxText()
        self.comboRole.append_text("Administrador")
        self.comboRole.append_text("Cliente")

        lblConf = Gtk.Label("Confirmar")
        txtConf = Gtk.Entry()
        txtConf.set_visibility(False)

        btnRegistro=Gtk.Button("Registrate")
        btnRegistro.connect("clicked",self.registro)

        boxH1.pack_start(lblUser,False,False,0)
        boxH1.pack_start(self.txtUser,False,False,0)
        boxH1.pack_start(lblPass, False, False, 0)
        boxH1.pack_start(self.txtPass, False, False, 0)

        boxH2.pack_start(lblCombo, False, False, 0)
        boxH2.pack_start(self.comboRole,False,False,0)
        boxH2.pack_start(lblConf, False, False, 0)
        boxH2.pack_start(txtConf,False,False,0)

        boxFin.pack_start(btnRegistro,False,False,0)

        mainBox.pack_start(boxH1,False,False,0)
        mainBox.pack_start(boxH2, False, False, 0)
        mainBox.pack_start(boxFin, False, False, 0)


        self.add(mainBox)
        self.show_all()
    def registro(self,boton):
        print("Registrando")

        cc=FuncionesDB.selectCodU(self)
        codigo=0
        for codu in cc:
            if(codu is not None):
                if(codigo<=codu):
                    codigo=codu
        codigo=codigo+1
        FuncionesDB.insert(self.fc,codigo,self.txtUser.get_text(),self.txtPass.get_text(),self.comboRole.get_active_text())




