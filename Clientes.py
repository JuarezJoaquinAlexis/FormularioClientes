from Conexion import *

class CClientes:

    def mostrarClientes():

        try:
         cone = CConexion.ConexionBaseDeDatos()
         cursor = cone.cursor()
         cursor.execute ("SELECT id, nombres, apellidos, sexo, numero_documento, fecha_nacimiento, telefono, domicilio FROM usuarios;") 
         miResultado = cursor.fetchall()
         cone.close()
         return miResultado
        
        except mysql.connector.Error as error:
            print("Error de mostrar datos {}".format(error))
            return []




    def ingresarClientes(nombres,apellidos,sexo, documento, fecha_nacimiento, telefono, domicilio):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql ="""
         INSERT INTO usuarios (nombres, apellidos, sexo, numero_documento, fecha_nacimiento, telefono, domicilio)
         VALUES (%s, %s, %s, %s, %s, %s, %s);
         """
            #La variable valores, tupla (array que no se modifica)
            #Minima expresion:(valor,) la , hace que sea una tupla 
            #tupla = listas inmutables, no se modifican
            valores = (nombres, apellidos, sexo, documento, fecha_nacimiento, telefono, domicilio)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            cone.close()



        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))

    def modificarClientes(idUsuario,nombres,apellidos,sexo, documento, fecha_nacimiento, telefono, domicilio):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql ="""
         UPDATE usuarios
         SET nombres = %s, apellidos = %s, sexo = %s, numero_documento = %s, 
            fecha_nacimiento = %s, telefono = %s, domicilio = %s
         WHERE id = %s;
         """
            valores = (nombres, apellidos, sexo, documento, fecha_nacimiento, telefono, domicilio, idUsuario)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
            cone.close()



        except mysql.connector.Error as error:
            print("Error de actualizacion de datos {}".format(error))
        
        
    def eliminarClientes(idUsuario):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql ="DELETE from usuarios WHERE usuarios.id= %s;"
            valores = (idUsuario,)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            cone.close()



        except mysql.connector.Error as error:
            print("Error de eliminacion de datos {}".format(error))