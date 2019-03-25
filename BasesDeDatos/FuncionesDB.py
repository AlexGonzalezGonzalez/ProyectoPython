from sqlite3 import dbapi2

class FuncionesDB:

    def __init__(self):
        self.bbdd = dbapi2.connect("BasesDeDatos/Usuarios.db")
        #self.bbdd.execute("create table Usuarios(codu number, nomu text,pass text, role text)")

    def selectCodU(self):
        """Metodo que devuelve una lista con los codigos de los usuarios"""
        cursor = self.bbdd.cursor()
        cursor.execute("select codu from Usuarios")
        listaCodigos=list()
        for codu in cursor:
            listaCodigos.append(codu)
        return listaCodigos

    def selectNomU(self):
        """Metodo que devuelve una lista con los nombres de los usuarios"""
        cursor = self.bbdd.cursor()
        cursor.execute("select nomu from Usuarios")
        listaNombres=list()
        for codu in cursor:
            listaNombres.append(codu)
        return listaNombres

    def selectPassU(self):
        """Metodo que devuelve una lista con las contraseñas de los usuarios"""
        cursor = self.bbdd.cursor()
        cursor.execute("select pass from Usuarios")
        listaPassword=list()
        for codu in cursor:
            listaPassword.append(codu)
        return listaPassword

    def selectRoleU(self):
        """Metodo que devuelve una lista con los roles de los usuarios"""
        cursor = self.bbdd.cursor()
        cursor.execute("select role from Usuarios")
        listaRoles=list()
        for codu in cursor:
            listaRoles.append(codu)
        return listaRoles

    def selectCodUWhere(self,campo,valor):
        """Metodo que devuelve una lista con los codigos de los usuarios que coincidan a la condicion dada"""
        cursor = self.bbdd.cursor()
        cursor.execute("select codu from Usuarios where "+campo+" = '"+valor+"';")
        listaCodigos=list()
        for codu in cursor:
            listaCodigos.append(codu)
        return listaCodigos

    def selectNomUWhere(self,campo,valor):
        """Metodo que devuelve una lista con los nombres de los usuarios que coincidan a la condicion dada"""
        cursor = self.bbdd.cursor()
        cursor.execute("select nomu from Usuarios where " + campo + " = '" + valor + "';")
        listaNombres=list()
        for codu in cursor:
            listaNombres.append(codu)
        return listaNombres

    def selectPassUWhere(self,campo,valor):
        """Metodo que devuelve una lista con las contraseñas de los usuarios que coincidan a la condicion dada"""
        cursor = self.bbdd.cursor()
        cursor.execute("select pass from Usuarios where " + campo + " = '" + valor + "';")
        listaPassword=list()
        for codu in cursor:
            listaPassword.append(codu)
        return listaPassword

    def selectRoleUWhere(self,campo,valor):
        """Metodo que devuelve una lista con los roles de los usuarios que coincidan a la condicion dada"""
        cursor = self.bbdd.cursor()
        cursor.execute("select role from Usuarios where " + campo + " = '" + valor + "';")
        listaRoles=list()
        for codu in cursor:
            listaRoles.append(codu)
        return listaRoles

    def insert(self,codu,nomu,passw,role):
        """Metodo que inserta en la tabla Usuarios los valores dados"""
        cursor = self.bbdd.cursor()
        cursor.execute("insert into Usuarios values("+str(codu)+",'"+str(nomu)+"','"+str(passw)+"', '"+str(role)+"')")

    def selectAll(self):
        listaAll=list()
        cursor = self.bbdd.cursor()
        cursor.execute("select codu,nomu,pass,role from Usuarios")

        for linea in cursor:
            subLista = list()

            for campo in linea:
                subLista.append(campo)

        listaAll.append(subLista)

        return listaAll

