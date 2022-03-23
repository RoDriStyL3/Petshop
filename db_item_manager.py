import sqlite3
import os
from tkinter import messagebox
from tkinter import *

###### clase para manejo de inventario #####
#root = Tk()
class db_item_manager_class():
	APP_PATH_ITEM = os.getcwd() + "/item_manager.db"
	
	def __init__(self):
		self.connection = sqlite3.connect(self.APP_PATH_ITEM)
		self.cursor = self.connection.cursor()
		try:
			self.cursor.execute("CREATE TABLE ITEMS (COD_INT VARCHAR(50) PRIMARY KEY, COD_EXT VARCHAR(50), FACTURA VARCHAR (50), NOMBRE VARCHAR (50), DESCRIPCION VARCHAR(100), PRESENTACION VARCHAR(20), PROVEEDOR VARCHAR(50),  FECHA_ACCION VARCHAR (20), CANT_CAJA INTEGER, CANT_UNI INTEGER, PREC_CAJA FLOAT, PREC_UNI FLOAT, PREC_VE_CAJA FLOAT, PREC_VE_UNI FLOAT, TIPO_ACCION VARCHAR(10), TIPO_SALIDA VARCHAR(20), RESPONSABLE VARCHAR(20))")
			self.connection.commit()
		except:
				pass
					
	def insert_values(self, lista_items):
		self.connection = sqlite3.connect(self.APP_PATH_ITEM)
		self.cursor = self.connection.cursor()
		self.cursor.executemany("INSERT INTO ITEMS VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", [lista_items])
		self.connection.commit()
		
		
	def buscar_item_nombre(self, nombre):
		self.nombre = nombre
		conex = sqlite3.connect(self.APP_PATH_ITEM)
		puntero = conex.cursor()
		query = (f"SELECT COD_INT, DESCRIPCION FROM ITEMS WHERE NOMBRE LIKE ? ")
		puntero.execute(query, [f'{self.nombre}%'])
		consulta = puntero.fetchall()
		return consulta
	
	
	def buscar_item_codigo(self, codigo):
		self.codigo = codigo
		conex = sqlite3.connect(self.APP_PATH_ITEM)
		puntero = conex.cursor()
		query = (f"SELECT COD_INT, DESCRIPCION FROM ITEMS WHERE COD_INT LIKE ? ")
		puntero.execute(query, [f'{self.codigo}%'])
		consulta = puntero.fetchall()
		return consulta
		
		
		
		
	def set_inputs_frame_modificador(self, codigo):
		self.datos = []
		self.codigo = codigo
		conex = sqlite3.connect(self.APP_PATH_ITEM)
		puntero = conex.cursor()
		query = (f"SELECT * FROM ITEMS WHERE COD_INT LIKE ? ")
		puntero.execute(query, [f'{self.codigo}%'])
		consulta = puntero.fetchall()
		return consulta
		#####Base de datos de usuario#####
		
		
	def update_item(self, nombre, datos):
		self.nombre = nombre
		#self.codigo = codigo
		self.datos = datos
		conex = sqlite3.connect(self.APP_PATH_ITEM)
		puntero = conex.cursor()
		puntero.execute (f"UPDATE ITEMS SET NOMBRE = ?, DESCRIPCION = ?, COD_EXT = ?, COD_INT = ?,FACTURA = ?, PRESENTACION = ?, PROVEEDOR = ?, FECHA_ACCION = ?, CANT_CAJA = ?, CANT_UNI = ?, PREC_CAJA = ?, PREC_UNI = ?, PREC_VE_CAJA = ?, PREC_VE_UNI = ?, TIPO_ACCION = ?, TIPO_SALIDA = ?, RESPONSABLE = ? WHERE NOMBRE = '{self.nombre}' ", (self.datos))
		conex.commit()
		messagebox.showinfo("GUARDADO.", "¡CAMBIOS GUARDADOS CON ÉXITO!")
		#puntero.execute(query, [f'{self.datos}, {self.nombre}'])
		


###### Clase para manejo de usuarios ######
class db_user_manager_class():
	
	lista_consultas = []
	
	APP_PATH = os.getcwd() + "/User_list.db"

	def insert_user_values(self, lista_datos):
			
			conex = sqlite3.connect(self.APP_PATH)
			puntero = conex.cursor()
			
			try:
				puntero.execute("CREATE TABLE USERS (NOMBRE VARCHAR (50), PASSWORD VARCHAR (20), RESPONSABLE VARCHAR(50), CARGO VARCHAR(50))")
				conex.commit()
			except:
				pass
			conex = sqlite3.connect(self.APP_PATH)
			puntero = conex.cursor()
			puntero.execute("INSERT INTO USERS VALUES(?,?,?,?)", lista_datos)
			conex.commit()
			
	def validar_usuario(self):
		conex = sqlite3.connect(self.APP_PATH)
		puntero = conex.cursor()
		puntero.execute("SELECT * FROM USERS")
		lista_consultas = puntero.fetchall()			
		return lista_consultas		
	
		
#item = db_item_manager_class()
#consulta = item.set_inputs_frame_modificador('r68')
#for i in consulta:
#	messagebox.showinfo("", (i[3]))
#	
#root.mainloop()