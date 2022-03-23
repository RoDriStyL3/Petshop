#import sqlite3
#from tkinter import *
#from tkinter import messagebox
#from tkinter.ttk import Combobox
#from Users_GUI import *
#import datetime

#class AlmacenClass():
#	
#	
#	def __init__(self, root):
#		self.root = root
#		#self.btn_Almacen = Button(self.root, text = "Almacen", bg = "#DCDCDC", command = lambda : self.crear_frame_almacen())
#		#self.btn_Almacen.place(x = 100, y = 200)
#		self.btn_Almacen = Button()
#		self.frm_almacen = Frame()
#		self.frm_ingreso_item = Frame()
#		self.cantxCajaVar = StringVar()
#		self.precxCajaVar = StringVar()
#		self.calcPrecxUnd = StringVar()
#				
#								
#	def borrar(self, frame_borra):
#		self.frame = frame_borra
#		self.frame.place_forget()		
#		
#		
#	##### Frame Almacen ####	
#	def crear_frame_almacen(self):
#		self.borrar(self.btn_Almacen)
#		self.frm_almacen = Frame(self.root, width = 850, height = 1000, bg = "#ADD8E6")
#		self.frm_almacen.place(x = 10, y = 100)
#		
#		self.btn_Almacen = Button(self.root, text = "Almacen", bg = "#DCDCDC", command = lambda : self.crear_frame_almacen())
#		self.btn_Almacen.place(x = 100, y = 200)
#	###### Botones de almacen #######
#		
#		self.lbl_almacen = Label(self.frm_almacen, text = "Almacen", bg = "skyblue", width = 15, height = 1, font = ("Arial", 10))
#		self.lbl_almacen.place(x = 50, y = 100)
#		
#		self.btn_ingresar_item = Button(self.frm_almacen, text = "Ingresar producto", bg = "#DCDCDC", width = 10, command = lambda : self.crear_frame_ingreso_item())
#		self.btn_ingresar_item.place(x = 50, y = 250)
#		
#		self.lbl_ingresar_item = Label(self.frm_almacen, text = '(Administrador)', bg = "red")
#		self.lbl_ingresar_item.place(x = 480, y = 270)
#		
#		self.btn_modificar_item = Button(self.frm_almacen, text = "Modificar producto", bg = "#DCDCDC", width = 10)
#		self.btn_modificar_item.place(x = 50, y = 400)
#		
#		self.lbl_modificar_item = Label(self.frm_almacen, text = '(Administrador)', bg = "red")
#		self.lbl_modificar_item.place(x = 480, y = 420)
#		
#		self.btn_consultar_item = Button(self.frm_almacen, text = "Consultar producto", bg = "#DCDCDC", width = 10)
#		self.btn_consultar_item.place(x = 50, y = 550)
#		
#		self.btn_consultar_inventario = Button(self.frm_almacen, text = "Ver inventario", bg = "#DCDCDC", width = 10)
#		self.btn_consultar_inventario.place(x = 50, y = 700)
#		
#		return self.frm_almacen
#		
#		
#	###### Frame Ingreso items ######
#	
#	def crear_frame_ingreso_item(self):
#		self.borrar(self.frm_almacen)
#		self.frm_ingreso_item = Frame(self.root, bg = "#778899", width = 1200, height = 2500)
#		self.frm_ingreso_item.place(x = 150, y = 200)
#		
#		self.lbl_ingreso_item_titulo = Label(self.frm_ingreso_item, text = "INGRESO DE PRODUCTO NUEVO", bg = "#ADD8E6")
#		self.lbl_ingreso_item_titulo.place(x = 250, y = 50)
#		
#		
#		self.lbl_ingreso_item_cod_int = Label(self.frm_ingreso_item, text = "Cod. Int.", bg = "#ADD8E6", width = 7)
#		self.lbl_ingreso_item_cod_int.place(x = 240, y = 150)
#		
#		self.entry_ingreso_item_cod_int = Entry(self.frm_ingreso_item)
#		self.entry_ingreso_item_cod_int.place(x = 240, y = 205, width = 195)
#		
#		
#		self.lbl_ingreso_item_cod_ext = Label(self.frm_ingreso_item, text = "Cod. Ext.", bg = "#ADD8E6", width = 7)
#		self.lbl_ingreso_item_cod_ext.place(x = 540, y = 150)
#		
#		self.entry_ingreso_item_cod_ext = Entry(self.frm_ingreso_item)
#		self.entry_ingreso_item_cod_ext.place(x = 540, y = 205, width = 195)
#		
#		
#		
#		
#		self.lbl_ingreso_item_nombre = Label(self.frm_ingreso_item, text = "NOMBRE", bg = "#ADD8E6", width = 25)
#		self.lbl_ingreso_item_nombre.place(x = 300, y = 400)
#		
#		self.entry_ingreso_item_nombre = Entry(self.frm_ingreso_item)
#		self.entry_ingreso_item_nombre.place(x = 240, y = 455, width = 800)
#		
#		
#		self.lbl_ingreso_item_descrip= Label(self.frm_ingreso_item, text = "DESCRIPCION", bg = "#ADD8E6", width = 25)
#		self.lbl_ingreso_item_descrip.place(x = 300, y = 600)
#		
#		self.entry_ingreso_item_descrip = Entry(self.frm_ingreso_item)
#		self.entry_ingreso_item_descrip.place(x = 240, y = 655, width = 800)
#		
#		
#		
#		
#		self.lbl_ingreso_item_presen = Label(self.frm_ingreso_item, text = "PRESENTACIÓN", bg = "#ADD8E6", width = 25)
#		self.lbl_ingreso_item_presen.place(x = 300, y = 800)
#		
#		self.cmbox_ingreso_item_presen = Combobox(self.frm_ingreso_item, values = ["Caja", "Bulto", "Saco"], state = "readonly")
#		self.cmbox_ingreso_item_presen.current(0)
#		self.cmbox_ingreso_item_presen.place(x = 240, y = 855, width = 800)
#		
#		self.lbl_cant_xCaja = Label(self.frm_ingreso_item, text = "×", bg = "#778899")
#		
#		self.lbl_cant_xCaja.place(x = 240, y = 920)	
#		
#		
#		self.entry_cant_xCaja = Entry(self.frm_ingreso_item, textvariable = self.cantxCajaVar)
#		self.entry_cant_xCaja.place(x = 275, y = 920, width = 100)
#		
#		self.lbl_cant_xCaja_und = Label(self.frm_ingreso_item, text = "unds", bg = "#778899")		
#		self.lbl_cant_xCaja_und.place(x = 380, y = 920)
#		
#		
#		
#		
#		self.lbl_ingreso_item_proveedor = Label(self.frm_ingreso_item, text = "PROVEEDOR", bg = "#ADD8E6", width = 25)
#		self.lbl_ingreso_item_proveedor.place(x = 300, y = 1060)
#		
#		self.entry_ingreso_item_proveedor = Entry(self.frm_ingreso_item)
#		self.entry_ingreso_item_proveedor.place(x = 240, y = 1115, width = 800)
#		
#	
#		
#				
#		self.lbl_ingreso_item_precCosto = Label(self.frm_ingreso_item, text = "PRECIO COSTO(CAJA)", bg = "#ADD8E6", width = 25)
#		self.lbl_ingreso_item_precCosto.place(x = 300, y = 1260)
#		
#		self.entry_ingreso_item_precCosto = Entry(self.frm_ingreso_item, textvariable = self.precxCajaVar)
#		self.entry_ingreso_item_precCosto.place(x = 240, y = 1315, width = 800)
#		

#		
#						
#		self.lbl_ingreso_item_precCostoUnd = Label(self.frm_ingreso_item, text = "PRECIO COSTO(UNIDAD)", bg = "#ADD8E6", width = 25)
#		self.lbl_ingreso_item_precCostoUnd.place(x = 300, y = 1460)
#		
#		self.entry_ingreso_item_precCostoUnd = Entry(self.frm_ingreso_item, textvariable = self.calcPrecxUnd)
#		self.entry_ingreso_item_precCostoUnd.place(x = 240, y = 1515, width = 800)
#		
#		
#		
#		self.btn_auto_precCostoUnd = Button(self.frm_ingreso_item, text = "Auto.", command = lambda : self.calcular_auto_precCostoUnd())
#		self.btn_auto_precCostoUnd.place(x = 240, y = 1580, width = 130, height = 70)
#		
#	
#		
#				
#		self.lbl_ingreso_item_precVentaCaja = Label(self.frm_ingreso_item, text = "PRECIO DE VENTA (CAJA)", bg = "#ADD8E6", width = 25)
#		self.lbl_ingreso_item_precVentaCaja.place(x = 300, y = 1735)
#		
#		self.entry_ingreso_item_precVentaCaja = Entry(self.frm_ingreso_item)
#		self.entry_ingreso_item_precVentaCaja.place(x = 240, y = 1795, width = 800)
#		
#		
#		
#		
#		self.lbl_ingreso_item_precVentaUnd = Label(self.frm_ingreso_item, text = "PRECIO DE VENTA (UNIDAD)", bg = "#ADD8E6", width = 25)
#		self.lbl_ingreso_item_precVentaUnd.place(x = 300, y = 1935)
#		
#		self.entry_ingreso_item_precVentaUnd = Entry(self.frm_ingreso_item)
#		self.entry_ingreso_item_precVentaUnd.place(x = 240, y = 1990, width = 800)
#		
#		
#		self.btn_enviar_registro_item = Button(self.frm_ingreso_item, text = "GUARDAR PRODUCTO", bg = "#D3D3D3", command = lambda : self.guatdar_producto())
#		self.btn_enviar_registro_item.place(x = 140, y = 2140, width = 500)
#		
#		
#		self.btn_cancelar_registro_item = Button(self.frm_ingreso_item, text = "CANCELAR", bg = "#D3D3D3")
#		self.btn_cancelar_registro_item.place(x = 800, y = 2140, width = 300)
#		
#		
#		
###### Funcion calcular auto prec x und #####

#	def calcular_auto_precCostoUnd(self):
#		try:
#			self.calcPrecxUnd.set(round(float(self.precxCajaVar.get()) / float(self.cantxCajaVar.get()), 2))
#		except:
#			pass
#			
#			
#			
#	def guatdar_producto(self):
#		messagebox.askyesno("Petshop", "¿Desea guardar el nuevo producto?")
#		
#		