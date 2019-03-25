import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from sqlite3 import dbapi2
from ProyectoInmobiliaria.VentanaRegistro import VentanaRegistro
from ProyectoInmobiliaria.VentanaPrincipal import VentanaPrincipal
from ProyectoInmobiliaria.BasesDeDatos import FuncionesDB

class VentanaLogin(Gtk.Window):

    def __init__(self):

        print("Iniciando la Ventana Login")

        #Conexion a la base
        self.bbdd = dbapi2.connect("BasesDeDatos/Usuarios.db")
        #self.bbdd.execute("create table Usuarios(codu number, nomu text,pass text, role text)")

        #Iniciamos la ventana
        Gtk.Window.__init__(self, title="Login")

        #Le damos un tamaño
        self.resize(150,150)

        #Box que contiene todo
        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        #Componentes y caracteristicas de la ventana
        lblUser = Gtk.Label("Usuario")
        txtUser = Gtk.Entry()

        lblPass = Gtk.Label("Contraseña")
        txtPass = Gtk.Entry()
        txtPass.set_invisible_char("*")

        lblError= Gtk.Label()

        #Box para los botones registro y login
        secundaryBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing =  50)

        btnRegistro = Gtk.Button("Registrate")
        btnRegistro.connect("clicked",self.initVentanaRegistro)

        btnLogin = Gtk.Button("Log")
        btnLogin.connect("clicked",self.log,txtUser,txtPass,lblError)

        secundaryBox.pack_start(btnRegistro,False,False,0)
        secundaryBox.pack_start(btnLogin, False, False, 0)

        mainBox.pack_start(lblUser,False,False,0)
        mainBox.pack_start(txtUser, False, False, 0)
        mainBox.pack_start(lblPass, False, False, 0)
        mainBox.pack_start(txtPass, False, False, 0)
        mainBox.pack_start(lblError, False, False, 0)
        mainBox.pack_end(secundaryBox,False,False,0)

        self.add(mainBox)
        self.show_all()

    #Inicio de la ventana registro
    def initVentanaRegistro(self,boton):
        VentanaRegistro()

    #Inicio de la VentanaPrincipal si los datos son correctos
    def log(self,boton,usuario,password,error):

        cursor = self.bbdd.cursor()
        cursor.execute("select nomu,pass from Usuarios where nomu='"+str(usuario.get_text())+"' and pass='"+str(password.get_text())+"'")

        if(cursor.fetchall().__len__()<=1):
            VentanaPrincipal()
            print("Logueado")

        else:
            error.set_text("Error en el login")
            print("Error en el login")

if __name__ == '__main__':
    VentanaLogin()
Gtk.main()



