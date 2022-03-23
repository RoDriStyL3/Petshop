import datetime
import tkinter.font as tkFont
from tkinter import *
import sqlite3
import os
from db_item_manager import *
from tkinter import ttk
from tkinter.ttk import Combobox



class UsersClass():
	
	#responsableVar = 0
	gate_user = False
	puerta_admin = False
#	userVar = 0
#	passVar = 0
#	passVar2 = 0
#	cargoVar = 0
#	root = 0
#	btn_inicio_sesion = 0
	
	def borra(self, frame_borrado):
		frame = frame_borrado
		frame.place_forget()
		
	def borrar_frame_inicio(self):
		self.frame = self.frame_inicio_sesion
		self.frame.place_forget()


	def __init__(self, root):
		self.root = root
		self.root.config(width = 1200, height = 1200, bg = "#ADD8E6")
		self.opt = IntVar()
		self.fecha_hoy = datetime.datetime.now()
		self. mostrar_pass = False
		self.userVar = StringVar()
		self.responsableVar = StringVar()
		self.passVar = StringVar()
		self.passVar2 = StringVar()
		self.cargoVar = StringVar()
		self.APP_PATH = os.getcwd()
		self.admin = False
		self.user_gate = False
		self.crear_frame_inicio_sesion = Frame()
		self.btn_inicio_sesion = Button(self.root, text = "INICIO SESIÓN", command = lambda : [self.frame_inicio_sesion()], width = 30, height = 10)
		self.frame_registro = Frame()
		self.frame_mostrar_datos = Frame()		
		self.btn_inicio_sesion.place(x = 300, y = 800)
		
		
	def validar_datos_inicio(self):
		user = db_user_manager_class()		
		for i in user.validar_usuario():
			if i[0] == self.userVar.get() and i[1] == self.passVar.get():
				self.user_gate = True
				UsersClass.gate_user = True
				if str(i[0]) == "Admin":
					self.admin = True
					UsersClass.puerta_admin = self.admin
				self.responsableVar.set(str(i[2]))
				self.cargoVar.set(str(i[3]))
				break
			else:
				pass
				
		if self.user_gate == True:
			messagebox.showinfo("INICIO DE SESIÓN EXITOSO!", "Bienvenido " + str(i[2]))
			#self.responsableVar.set(str(i[2]))
			self.crear_frame_mostrar_datos()
			self.userVar.set("")
			self.passVar.set("")
			self.cargoVar.set("")
			MenuPrincipal(self.root, self.responsableVar.get(), self.user_gate, self.puerta_admin).crear_frame_principal_menu()
			self.responsableVar.set("")
			self.borra_inicio_sesion()
						
		else:
			messagebox.showerror("ERROR DE INICIO", "USUARIO O CONTRASEÑA INVALIDO")
		self.userVar.set("")
		self.passVar.set("")
		self.user_gate = False
		self.frame_inicio_sesion()
		self.gate_user = self.user_gate
		
	def frame_inicio_sesion (self):
		
		self.borrar_frame_registro()
		self.borra(self.btn_inicio_sesion)
		####Frame inicio#####
		self.crear_frame_inicio_sesion = Frame(self.root, width = 850, height = 1500, bg = "#ADD8E6")
		self.crear_frame_inicio_sesion.place(x=0,y=0)
		
		#### Ingreso credenciales ####
		
		  ### Usuario
		self.entry_ingreso_usuario = Entry(self.crear_frame_inicio_sesion, textvariable = self.userVar)
		self.entry_ingreso_usuario.place(x = 50, y = 200)
		
		lbl_ingreso_usuario= Label(self.crear_frame_inicio_sesion, text = "Usuario", bg = "skyblue")
		lbl_ingreso_usuario.place(x=450,y=200)
				
		
		  ###Password		  
		  
		def mostrar_passw():
			if self.mostrar_pass == False:
				self.mostrar_pass = True
			else:
				self.mostrar_pass = False
			
		def mostrar_password():
		  	self.entry_ingreso_password = Entry(self.crear_frame_inicio_sesion, textvariable = self.passVar)
		  	self.entry_ingreso_password.place(x = 50, y = 300)
		  	lbl_ingreso_password = Label(self.crear_frame_inicio_sesion, text = "Password", bg = "skyblue")
		  	lbl_ingreso_password.place(x = 450, y = 300)
		  	if self.mostrar_pass == False:
		  		self.entry_ingreso_password.config(show = "*")
		  		
		mostrar_password()
		
		btn = Button(self.crear_frame_inicio_sesion, text = "Enviar", bg = "#DCDCDC", command = lambda : [self.validar_datos_inicio(), self.borra(self.crear_frame_inicio_sesion)])
		btn.place(x=400,y=800)
		
				###Mostrar pass		
		self.chk_btn_mostrar_pass = Checkbutton(self.crear_frame_inicio_sesion, text = "Mostrar contraseña.", variable = self.mostrar_pass, command = lambda : [mostrar_passw(), mostrar_password()], bg = "#ADD8E6")
		self.chk_btn_mostrar_pass.place(x = 50, y = 400)
		
	def borra_inicio_sesion(self):
		self.frame = self.crear_frame_inicio_sesion
		self.frame.place_forget()

########## CERRAR SESIÓN #########
	
	def cerrar_sesion(self):
		self.borrar_mostrar_datos()
		self.user_gate = False
		UsersClass.gate_user = False
		self.gate_user = self.user_gate
		self.frame_inicio_sesion()
					
########## MOSTRAR DATOS ######

	def crear_frame_mostrar_datos(self):
		self.frame_mostrar_datos = Frame(self.root, width = 500, height = 200, bg = "skyblue")
		self.frame_mostrar_datos.place(x = 900, y = 30)
		self.lbl_mostrar_datos_user = Label(self.frame_mostrar_datos, text = self.responsableVar.get(), bg = "skyblue")
		self.lbl_mostrar_datos_user.place(x = 20, y = 20)	
		
		self.responsableFunc()
		
		self.lbl_mostrar_datos_cargo = Label(self.frame_mostrar_datos, text = self.cargoVar.get(), bg = "skyblue")
		self.lbl_mostrar_datos_cargo.place(x = 20, y = 80)
		
		self.fecha_actual = datetime.datetime.strftime(self.fecha_hoy, "%d, %b, %Y")
		self.lbl_mostrar_datos_fecha = Label(self.frame_mostrar_datos, text = self.fecha_actual, bg = "skyblue")
		self.lbl_mostrar_datos_fecha.place(x = 20, y = 140)
		
		return self.responsableVar.get()
		
	
	
	def responsableFunc(self):
		responsableVarAux = StringVar()
		responsableVarAux = set(self.responsableVar.get())
		
	def borrar_mostrar_datos(self):
		self.frame_mostrar_datos.place_forget()
		
						
####### REGISTRO USUARIO ######		
	def crear_frame_registro(self, puerta, puerta2):
		self.puerta = puerta
		self.puerta2 = puerta2		
		
		if self.puerta == False or self.puerta2 == False:
			messagebox.showerror("ERROR", "DEBE INICIAR SESIÓN  \nCOMO ADMINISTRADOR")
		else:
			self.borra_inicio_sesion()
			#self.borra(self.btn_inicio_sesion)
			#self.borra(AlmacenClass.crear_frame_almacen)
			self.frame_registro = Frame(self.root, width = 850, height = 1500, bg = "#ADD8E6")
			self.frame_registro.place(x = 20, y = 20)
			
			
			self.entry_user_registro = Entry(self.frame_registro, textvariable = self.userVar)
			self.entry_user_registro.place(x = 10, y = 10, width = 400)
			
			self.lbl_user_registro = Label(self.frame_registro, text = "Usuario", bg = "skyblue")
			self.lbl_user_registro.place(x = 350, y = 10)
			
			self.entry_pass_registro = Entry(self.frame_registro, show = "*", textvariable = self.passVar)
			self.entry_pass_registro.place(x = 10, y = 100, width = 400)
			
			self.lbl_pass_registro = Label(self.frame_registro, text = "Contraseña", bg = "skyblue")
			self.lbl_pass_registro.place(x = 350, y = 100)
			
			self.entry_pass2_registro = Entry(self.frame_registro, show = "*", textvariable = self.passVar2)
			self.entry_pass2_registro.place(x = 10, y = 180)
			
			
			self.lbl_pass2_registro = Label(self.frame_registro, text = "Repetir contraseña", bg = "skyblue")
			self.lbl_pass2_registro.place(x = 350, y = 180)
		
		self.entry_responsable_registro = Entry(self.frame_registro, textvariable = self.responsableVar)
		self.entry_responsable_registro.place(x = 10, y = 280)
			
			
		self.lbl_responsable_registro = Label(self.frame_registro, text = "Responsable", bg = "skyblue")
		self.lbl_responsable_registro.place(x = 350, y = 280)
		self.entry_cargo_registro = Entry(self.frame_registro, textvariable = self.cargoVar)
		self.entry_cargo_registro.place(x = 10, y = 380, width = 400)
			
			
		self.lbl_cargo_registro = Label(self.frame_registro, text = "Cargo", bg = "skyblue")
		self.lbl_cargo_registro.place(x = 350, y = 380)
		
				
						
		self.btn_enviar_registro = Button(self.frame_registro, text = "Registrar", bg = "#DCDCDC", command = lambda : self.registrar())
		self.btn_enviar_registro.place(x = 350, y = 600, height = 100)
		
		
		
		self.btn_volver_reg = Button(self.frame_registro, text = "Volver", command = lambda : [self.frame_registro.place_forget(), self.crear_frame_menu_usuario(self.user_gate, self.puerta_admin)])
		self.btn_volver_reg.place(x = 50, y = 600)
		
	def borrar_frame_registro(self):
		self.frame = self.frame_registro
		self.frame.place_forget()
		
				
	def registrar (self):
		self.user = db_user_manager_class()
		try:
			for i in self.user.validar_usuario():
				if i[0] == self.userVar.get():
					messagebox.showerror("ERROR DE REGISTRO", "NOMBRE DE USUARIO OCUPADO")
					self.user_gate = False
					break
				elif len(self.userVar.get()) < 4:
					messagebox.showerror('ERROR', "NOMBRE INVÁLIDO, MUY CORTO.")
					self.user_gate = False
					break
					pass		
				else:
					self.user_gate = True
					
			if self.passVar.get() != self.passVar2.get():
				messagebox.showerror("ERROR AL REGISTRAR", "CONTRASEÑAS NO COINCIDEN")
			elif self.user_gate == True:
				self.lista_datos = [self.userVar.get(), self.passVar.get(), self.responsableVar.get(), self.cargoVar.get()]
				self.user.insert_user_values(self.lista_datos)
				messagebox.showinfo("REGISTRO EXITOSO", "¡USUARIO REGISTRADO CON ÉXITO!")
		except:
			messagebox.showerror("ERROR", "ERROR")

##############Frame menu Usuario ######

	def crear_frame_menu_usuario(self, gate, admin):
		self.gate_mu = gate
		self.admin_mu = admin
		
		self.borra(self.btn_inicio_sesion)
		#self.borra(self.btn_salir)
		
		self.frm_user_menu = Frame(self.root, width = 850, height = 1500, bg = "#778899")
		self.frm_user_menu.place(x = 10, y = 100)
		
		self.lbl_user_menu= Label(self.frm_user_menu, text = "Usuario", bg = "skyblue", width = 15, height = 1, font = ("Arial", 10))
		self.lbl_user_menu.place(x = 50, y = 100)
		
		
		self.btn_registrar_user = Button(self.frm_user_menu, text = "Registrar usuario", bg = "#DCDCDC", width = 10, command = lambda : [self.crear_frame_registro(self.gate_user, self.admin_mu), self.frm_user_menu.place_forget()])
		self.btn_registrar_user.place(x = 50, y = 250)
		
		self.lbl_registrar_admin_needed = Label(self.frm_user_menu, text = '(Administrador)', bg = "red")
		self.lbl_registrar_admin_needed.place(x = 480, y = 270)
		
		
		
		self.btn_cambiar_contrase = Button(self.frm_user_menu, text = "Editar usuario", bg = "#DCDCDC", width = 10)
		self.btn_cambiar_contrase.place(x = 50, y = 400)
		
		self.lbl_cambiar_con_admin_needed = Label(self.frm_user_menu, text = '(Administrador)', bg = "red")
		self.lbl_cambiar_con_admin_needed.place(x = 480, y = 420)
		
		
		
		self.btn_cerrar_sesion_user = Button(self.frm_user_menu, text = "Cerrar sesión", bg = "#DCDCDC", width = 10, command = lambda : [self.cerrar_sesion(), self.frm_user_menu.place_forget()])
		self.btn_cerrar_sesion_user.place(x = 50, y = 550)
		
		
		self.btn_salir = Button(self.frm_user_menu, text = "SALIR", command = lambda : self.root.destroy())	
		self.btn_salir.place(x = 500, y = 1200)
		
		self.btn_volver = Button(self.frm_user_menu, text = "Volver", command = lambda : [self.frm_user_menu.place_forget(), MenuPrincipal(self.root, self.responsableVar.get(), UsersClass.gate_user, UsersClass.puerta_admin).crear_frame_principal_menu()])
		self.btn_volver.place(x = 100, y = 1200)



class AlmacenClass(UsersClass):
	
	
	def __init__(self, root, responsable):
		
		self.root = root
		self.btn_Almacen = Button()
		self.frm_almacen = Frame()
		self.frm_ingreso_item = Frame()
		self.cantxCajaVar = StringVar()
		self.precxCajaVar = StringVar()
		self.calcPrecxUnd = StringVar()
		self.cod_ext = StringVar()
		self.cod_int = StringVar()
		self.nombre = StringVar()
		self.descripcion = StringVar()
		self.proveedor = StringVar()
		self.presentacion = StringVar()
		self.cant_caja = StringVar()
		self.cant_uni = StringVar()
		self.prec_caja = StringVar()
		self.prec_uni = StringVar()
		self.tipo_accion = StringVar()
		self.responsable = StringVar()
		self.factura = StringVar()
		self.prec_venta_caja = StringVar()
		self.prec_venta_uni = StringVar()
		self.tipo_salida = StringVar()
		self.fecha_hoy = datetime.datetime.now()
		self.fecha_actual = datetime.datetime.strftime(self.fecha_hoy, "%d, %b, %Y")
		self.respo = responsable
		self.responsableAlmacen = self.respo
		self.nombre_buscar = StringVar()
								
	def borrar(self, frame_borra):
		self.frame = frame_borra
		self.frame.place_forget()
		
		
	##### Frame Almacen ####	
	def crear_frame_almacen(self):
		#self.borrar(self.btn_Almacen)vv
		self.item = db_item_manager_class()
		self.frm_almacen = Frame(self.root, width = 850, height = 1200, bg = "#778899")
		self.frm_almacen.place(x = 10, y = 100)
		
		#self.btn_Almacen = Button(self.root, text = "Almacen", bg = "#DCDCDC", command = lambda : self.crear_frame_almacen())
#		self.btn_Almacen.place(x = 100, y = 200)
	###### Botones de almacen #######
		
		self.lbl_almacen = Label(self.frm_almacen, text = "Almacen", bg = "skyblue", width = 15, height = 1, font = ("Arial", 10))
		self.lbl_almacen.place(x = 50, y = 100)
		
		self.btn_ingresar_item = Button(self.frm_almacen, text = "Ingresar producto", bg = "#DCDCDC", width = 10, command = lambda : self.crear_frame_ingreso_item())
		self.btn_ingresar_item.place(x = 50, y = 250)
		
		self.lbl_ingresar_item = Label(self.frm_almacen, text = '(Administrador)', bg = "red")
		self.lbl_ingresar_item.place(x = 480, y = 270)
		
		self.btn_modificar_item = Button(self.frm_almacen, text = "Modificar producto", bg = "#DCDCDC", width = 10, command = lambda : self.crear_frame_mod_item())
		self.btn_modificar_item.place(x = 50, y = 400)
		
		self.lbl_modificar_item = Label(self.frm_almacen, text = '(Administrador)', bg = "red")
		self.lbl_modificar_item.place(x = 480, y = 420)
		
		self.btn_consultar_item = Button(self.frm_almacen, text = "Consultar producto", bg = "#DCDCDC", width = 10, command = lambda : self.crear_frm_buscar_item() )
		self.btn_consultar_item.place(x = 50, y = 550)
		
		self.btn_consultar_inventario = Button(self.frm_almacen, text = "Ver inventario", bg = "#DCDCDC", width = 10)
		self.btn_consultar_inventario.place(x = 50, y = 700)
		
		
		self.btn_volver_alm = Button(self.frm_almacen, text = "Volver", command = lambda : [self.frm_almacen.place_forget(), MenuPrincipal(self.root, self.responsableAlmacen, UsersClass.gate_user, UsersClass.puerta_admin).crear_frame_principal_menu()])
		self.btn_volver_alm.place(x = 200, y = 1000)
		
		
	###### Frame Ingreso items ######
	
	def crear_frame_ingreso_item(self):
		self.borrar(self.frm_almacen)

		self.frm_ingreso_item = Frame(self.root, bg = "#778899", width = 1200, height = 2500)
		self.frm_ingreso_item.place(x = 150, y = 250)
		
		self.lbl_ingreso_item_titulo = Label(self.frm_ingreso_item, text = "INGRESO DE PRODUCTO NUEVO", bg = "#ADD8E6")
		self.lbl_ingreso_item_titulo.place(x = 250, y = 50)
		
		
		self.lbl_ingreso_item_cod_int = Label(self.frm_ingreso_item, text = "Cod. Int.", bg = "#ADD8E6", width = 7)
		self.lbl_ingreso_item_cod_int.place(x = 240, y = 150)
		
		self.entry_ingreso_item_cod_int = Entry(self.frm_ingreso_item, textvariable = self.cod_int)
		self.entry_ingreso_item_cod_int.place(x = 240, y = 205, width = 195)
		
		
		self.lbl_ingreso_item_cod_ext = Label(self.frm_ingreso_item, text = "Cod. Ext.", bg = "#ADD8E6", width = 7)
		self.lbl_ingreso_item_cod_ext.place(x = 540, y = 150)
		
		self.entry_ingreso_item_cod_ext = Entry(self.frm_ingreso_item, textvariable = self.cod_ext)
		self.entry_ingreso_item_cod_ext.place(x = 540, y = 205, width = 195)
		
		
		
		
		self.lbl_ingreso_item_nombre = Label(self.frm_ingreso_item, text = "NOMBRE", bg = "#ADD8E6", width = 25)
		self.lbl_ingreso_item_nombre.place(x = 300, y = 400)
		
		self.entry_ingreso_item_nombre = Entry(self.frm_ingreso_item, textvariable = self.nombre)
		self.entry_ingreso_item_nombre.place(x = 240, y = 455, width = 800)
		
		
		self.lbl_ingreso_item_descrip= Label(self.frm_ingreso_item, text = "DESCRIPCION", bg = "#ADD8E6", width = 25)
		self.lbl_ingreso_item_descrip.place(x = 300, y = 600)
		
		self.entry_ingreso_item_descrip = Entry(self.frm_ingreso_item, textvariable = self.descripcion)
		self.entry_ingreso_item_descrip.place(x = 240, y = 655, width = 800)
		
		
		
		
		self.lbl_ingreso_item_presen = Label(self.frm_ingreso_item, text = "PRESENTACIÓN", bg = "#ADD8E6", width = 25)
		self.lbl_ingreso_item_presen.place(x = 300, y = 800)
		
		self.cmbox_ingreso_item_presen = Combobox(self.frm_ingreso_item, values = ["Caja", "Bulto", "Saco"], state = "readonly", textvariable = self.presentacion)
		self.cmbox_ingreso_item_presen.current(0)
		self.cmbox_ingreso_item_presen.place(x = 240, y = 855, width = 800)
		
		self.lbl_cant_xCaja = Label(self.frm_ingreso_item, text = "×", bg = "#778899")
		
		self.lbl_cant_xCaja.place(x = 240, y = 920)
		self.entry_cant_xCaja = Entry(self.frm_ingreso_item, textvariable = self.cant_caja)
		self.entry_cant_xCaja.place(x = 275, y = 920, width = 100)
		
		self.lbl_cant_xCaja_und = Label(self.frm_ingreso_item, text = "unds", bg = "#778899")		
		self.lbl_cant_xCaja_und.place(x = 380, y = 920)
		
		
		
		
		self.lbl_ingreso_item_proveedor = Label(self.frm_ingreso_item, text = "PROVEEDOR", bg = "#ADD8E6", width = 25)
		self.lbl_ingreso_item_proveedor.place(x = 300, y = 1060)
		
		self.entry_ingreso_item_proveedor = Entry(self.frm_ingreso_item, textvariable = self.proveedor)
		self.entry_ingreso_item_proveedor.config(fg = "black")
		
		self.entry_ingreso_item_proveedor.place(x = 240, y = 1115, width = 800)
			
		
				
		self.lbl_ingreso_item_precCosto = Label(self.frm_ingreso_item, text = "PRECIO COSTO(CAJA)", bg = "#ADD8E6", width = 25)
		self.lbl_ingreso_item_precCosto.place(x = 300, y = 1260)
		
		self.entry_ingreso_item_precCosto = Entry(self.frm_ingreso_item, textvariable = self.prec_caja)
		self.entry_ingreso_item_precCosto.place(x = 240, y = 1315, width = 800)
		

		
						
		self.lbl_ingreso_item_precCostoUnd = Label(self.frm_ingreso_item, text = "PRECIO COSTO(UNIDAD)", bg = "#ADD8E6", width = 25)
		self.lbl_ingreso_item_precCostoUnd.place(x = 300, y = 1460)
		
		self.entry_ingreso_item_precCostoUnd = Entry(self.frm_ingreso_item, textvariable = self.calcPrecxUnd)
		self.entry_ingreso_item_precCostoUnd.place(x = 240, y = 1515, width = 800)
		
		
		
		self.btn_auto_precCostoUnd = Button(self.frm_ingreso_item, text = "Auto.", command = lambda : self.calcular_auto_precCostoUnd())
		self.btn_auto_precCostoUnd.place(x = 240, y = 1580, width = 130, height = 70)
		
	
		
				
		self.lbl_ingreso_item_precVentaCaja = Label(self.frm_ingreso_item, text = "PRECIO DE VENTA (CAJA)", bg = "#ADD8E6", width = 25)
		self.lbl_ingreso_item_precVentaCaja.place(x = 300, y = 1735)
		
		self.entry_ingreso_item_precVentaCaja = Entry(self.frm_ingreso_item, textvariable = self.prec_venta_caja)
		self.entry_ingreso_item_precVentaCaja.place(x = 240, y = 1795, width = 800)
		
		
		
		
		self.lbl_ingreso_item_precVentaUnd = Label(self.frm_ingreso_item, text = "PRECIO DE VENTA (UNIDAD)", bg = "#ADD8E6", width = 25)
		self.lbl_ingreso_item_precVentaUnd.place(x = 300, y = 1935)
		
		self.entry_ingreso_item_precVentaUnd = Entry(self.frm_ingreso_item, textvariable = self.prec_venta_uni)
		self.entry_ingreso_item_precVentaUnd.place(x = 240, y = 1990, width = 800)
		
		#mp = MenuPrincipal(self.root)
		
		self.btn_enviar_registro_item = Button(self.frm_ingreso_item, text = "GUARDAR PRODUCTO", bg = "#D3D3D3", command = lambda : self.guardar_producto())
		self.btn_enviar_registro_item.place(x = 140, y = 2140, width = 500)
		
		
		self.btn_cancelar_registro_item = Button(self.frm_ingreso_item, text = "CANCELAR", bg = "#D3D3D3", command = lambda : [self.crear_frame_almacen(), self.frm_ingreso_item.place_forget()])
		self.btn_cancelar_registro_item.place(x = 800, y = 2140, width = 300)
		
		
		
###### Funcion calcular auto prec x und #####

	def calcular_auto_precCostoUnd(self):
		try:
			self.calcPrecxUnd.set(round(float(self.prec_caja.get()) / float(self.cant_caja.get()), 2))
		except:
			pass
			
			
			
	def guardar_producto(self):
		self.responsable.set(self.responsableAlmacen)
		self.lista_datos_item = (self.cod_int.get(), self.cod_ext.get(), self.factura.get(), self.nombre.get(), self.descripcion.get(), self.presentacion.get(), self.proveedor.get(), self.fecha_actual, self.cant_caja.get(), self.cant_uni.get(), self.prec_caja.get(), self.prec_uni.get(), self.prec_venta_caja.get(), self.prec_venta_uni.get(), self.tipo_accion.get(), self.tipo_salida.get(), self.responsable.get())
		self.resp_guardar = messagebox.askyesno("Petshop", "¿Desea guardar el nuevo producto?")
		if self.resp_guardar == True:
			self.item.insert_values(self.lista_datos_item)
			messagebox.showinfo("INFO", "PRODUCTO GUARDADO EXITOSAMENTE.")


####################MODIFICAR######


	def crear_frame_mod_item(self):
		self.frm_almacen.place_forget()
		
		self.frm_mod_item = Frame(self.root, height = 2000, width = 1500, bg = "#ADD8E6")
		self.frm_mod_item.place(x = 0, y = 300)
		
		self.entry_busqueda_item = Entry(self.frm_mod_item, textvariable = self.nombre_buscar)
		self.entry_busqueda_item.place(x = 100, y = 100, height = 100)
		
		self.lbl_buscar_item = Label(self.frm_mod_item, text = "BUSCAR POR:", bg = "skyblue")
		self.lbl_buscar_item.place(x = 100, y = 250)
		
		self.btn_buscar_cod_item_mod = Button(self.frm_mod_item, text = "Código", command = lambda : self.buscar_item_codigo_fun())
		self.btn_buscar_cod_item_mod.place(x = 80, y = 350)
		
		self.btn_buscar_nom_item_mod = Button(self.frm_mod_item, text = "Nombre", command = lambda : self.buscar_item_nombre_fun())
		self.btn_buscar_nom_item_mod.place(x = 400, y = 350)
		
		#self.text_result_mod_item = Text(self.frm_mod_item, width = 50, height = 10)
#		self.text_result_mod_item.place(x = 100, y = 500)

##### TREEVIEW #####

		self.tv_result_mod_item = ttk.Treeview(self.frm_mod_item, columns = 3)
		self.tv_result_mod_item.place(x = 100, y = 800, width = 1200)
		self.tv_result_mod_item['columns'] = ('COD_INT',  'DESCRIPCION')
		
		self.s = ttk.Style()
		self.s.theme_use('clam')
		
		self.s.configure('Treeview', rowheight = 90)
		
		self.tv_result_mod_item.column('#0', width = 0, stretch = 0)
		self.tv_result_mod_item.column('COD_INT', anchor = CENTER, stretch = 0, width = 250)
		self.tv_result_mod_item.column('DESCRIPCION', anchor = CENTER, width = 10)
		
		
		
		
		self.tv_result_mod_item.heading('#0', text=' ', anchor=CENTER)
		self.tv_result_mod_item.heading('COD_INT', text='CÓDIGO.', anchor=CENTER)

		self.tv_result_mod_item.heading('DESCRIPCION', text='DESCRIPCION',anchor=CENTER)
		
		self.btn_tv = Button(self.frm_mod_item, text = "Select", command = lambda: self.select_row())
		self.btn_tv.place( x = 300, y = 1800)
		
		
		####### UPDATE ###!#!!
	def crear_frm_upd_item(self):
		self.frm_mod_item.place_forget()
		self.frm_upd_item = Frame(self.root, width = 1500, height = 2500, bg = "#778899")
		self.frm_upd_item.place(x = 0, y = 300)
		
		self.lbl_mod_item_cod_int = Label(self.frm_upd_item, text = "Cod. Int.", bg = "#ADD8E6", width = 7)
		self.lbl_mod_item_cod_int.place(x = 240, y = 150)
		
		self.entry_mod_item_cod_int = Entry(self.frm_upd_item, textvariable = self.cod_int)
		self.entry_mod_item_cod_int.place(x = 240, y = 205, width = 195)
		
		
		self.lbl_mod_item_cod_ext = Label(self.frm_upd_item, text = "Cod. Ext.", bg = "#ADD8E6", width = 7)
		self.lbl_mod_item_cod_ext.place(x = 540, y = 150)
		
		self.entry_mod_item_cod_ext = Entry(self.frm_upd_item, textvariable = self.cod_ext)
		self.entry_mod_item_cod_ext.place(x = 540, y = 205, width = 195)
		
		
		self.lbl_mod_item_nombre = Label(self.frm_upd_item, text = "NOMBRE", bg = "#ADD8E6", width = 25)
		self.lbl_mod_item_nombre.place(x = 300, y = 400)
		
		self.entry_mod_item_nombre = Entry(self.frm_upd_item, textvariable = self.nombre)
		self.entry_mod_item_nombre.place(x = 240, y = 455, width = 800)
		
		
		self.lbl_mod_item_descrip= Label(self.frm_upd_item, text = "DESCRIPCION", bg = "#ADD8E6", width = 25)
		self.lbl_mod_item_descrip.place(x = 300, y = 600)
		
		self.entry_mod_item_descrip = Entry(self.frm_upd_item, textvariable = self.descripcion)
		self.entry_mod_item_descrip.place(x = 240, y = 655, width = 800)
		
		
		
		
		self.lbl_mod_item_presen = Label(self.frm_upd_item, text = "PRESENTACIÓN", bg = "#ADD8E6", width = 25)
		self.lbl_mod_item_presen.place(x = 300, y = 800)
		
		self.cmbox_mod_item_presen = Combobox(self.frm_upd_item, values = ["Caja", "Bulto", "Saco"], state = "readonly", textvariable = self.presentacion)
		self.cmbox_mod_item_presen.current(0)
		self.cmbox_mod_item_presen.place(x = 240, y = 855, width = 800)
		
		self.lbl_cant_xCaja = Label(self.frm_upd_item, text = "×", bg = "#778899")
		
		self.lbl_cant_xCaja.place(x = 240, y = 920)
		self.entry_cant_xCaja = Entry(self.frm_upd_item, textvariable = self.cant_caja)
		self.entry_cant_xCaja.place(x = 275, y = 920, width = 100)
		
		self.lbl_cant_xCaja_und = Label(self.frm_upd_item, text = "unds", bg = "#778899")		
		self.lbl_cant_xCaja_und.place(x = 380, y = 920)
		
		
		
		
		self.lbl_mod_item_proveedor = Label(self.frm_upd_item, text = "PROVEEDOR", bg = "#ADD8E6", width = 25)
		self.lbl_mod_item_proveedor.place(x = 300, y = 1060)
		
		self.entry_mod_item_proveedor = Entry(self.frm_upd_item, textvariable = self.proveedor)
		self.entry_mod_item_proveedor.config(fg = "black")
		
		self.entry_mod_item_proveedor.place(x = 240, y = 1115, width = 800)
			
		
				
		self.lbl_mod_item_precCosto = Label(self.frm_upd_item, text = "PRECIO COSTO(CAJA)", bg = "#ADD8E6", width = 25)
		self.lbl_mod_item_precCosto.place(x = 300, y = 1260)
		
		self.entry_mod_item_precCosto = Entry(self.frm_upd_item, textvariable = self.prec_caja)
		self.entry_mod_item_precCosto.place(x = 240, y = 1315, width = 800)
		

		
						
		self.lbl_mod_item_precCostoUnd = Label(self.frm_upd_item, text = "PRECIO COSTO(UNIDAD)", bg = "#ADD8E6", width = 25)
		self.lbl_mod_item_precCostoUnd.place(x = 300, y = 1460)
		
		self.entry_mod_item_precCostoUnd = Entry(self.frm_upd_item, textvariable = self.calcPrecxUnd)
		self.entry_mod_item_precCostoUnd.place(x = 240, y = 1515, width = 800)
		
		
		
		self.btn_auto_precCostoUnd = Button(self.frm_upd_item, text = "Auto.", command = lambda : self.calcular_auto_precCostoUnd())
		self.btn_auto_precCostoUnd.place(x = 240, y = 1580, width = 130, height = 70)
		
	
		
				
		self.lbl_mod_item_precVentaCaja = Label(self.frm_upd_item, text = "PRECIO DE VENTA (CAJA)", bg = "#ADD8E6", width = 25)
		self.lbl_mod_item_precVentaCaja.place(x = 300, y = 1735)
		
		self.entry_mod_item_precVentaCaja = Entry(self.frm_upd_item, textvariable = self.prec_venta_caja)
		self.entry_mod_item_precVentaCaja.place(x = 240, y = 1795, width = 800)
		
		
		
		
		self.lbl_mod_item_precVentaUnd = Label(self.frm_upd_item, text = "PRECIO DE VENTA (UNIDAD)", bg = "#ADD8E6", width = 25)
		self.lbl_mod_item_precVentaUnd.place(x = 300, y = 1935)
		
		self.entry_mod_item_precVentaUnd = Entry(self.frm_upd_item, textvariable = self.prec_venta_uni)
		self.entry_mod_item_precVentaUnd.place(x = 240, y = 1990, width = 800)
		
		
		self.btn_enviar_registro_item = Button(self.frm_upd_item, text = "GUARDAR CAMBIO", bg = "#D3D3D3", command = lambda : self.mod_item())
		self.btn_enviar_registro_item.place(x = 140, y = 2140, width = 500)
		
		
		
		self.btn_cancelar_registro_item = Button(self.frm_upd_item, text = "CANCELAR", bg = "#D3D3D3", command = lambda : [self.crear_frame_almacen(), self.frm_upd_item.place_forget()])
		self.btn_cancelar_registro_item.place(x = 800, y = 2140, width = 300)
		
		
	def mod_item(self):
			
		if messagebox.askyesno("ATENCIÓN", "¿DESEA GUARDAR CAMBIOS?"):
			self.datos = (self.nombre.get(), self.descripcion.get(), self.cod_ext.get(), self.cod_int.get(), self.factura.get(), self.presentacion.get(), self.proveedor.get(), self.fecha_actual, self.cant_caja.get(), self.cant_uni.get(), self.prec_caja.get(), self.calcPrecxUnd.get(), self.prec_venta_caja.get(), self.prec_venta_uni.get(), None, None, self.responsable.get())
			self.modificador = db_item_manager_class()
			self.str_nombre = str(self.final_seleccionado[3])
			self.modificador.update_item(self.str_nombre, self.datos)
		else:
			messagebox.showinfo("", "Error")
			pass
		
		###############
		
		
	def select_row(self):
		self.crear_frm_upd_item()
		self.item = db_item_manager_class()
		
		self.selected = self.tv_result_mod_item.item(self.tv_result_mod_item.focus())['values']
		
		self.final_seleccionado = self.item.set_inputs_frame_modificador(self.selected[0])
		self.final_seleccionado = self.final_seleccionado[0]
		
		#self.datos_to_update = []
#		for i in self.final_seleccionado:
#			self.datos_to_update.append(i)
			
		
		
		######SET VALOR########
		
		self.nombre.set(self.final_seleccionado[3])
		self.descripcion.set(self.final_seleccionado[4])
		self.cod_ext.set(self.final_seleccionado[1])
		self.cod_int.set(self.final_seleccionado[0])
		self.factura.set(self.final_seleccionado[2])
		self.presentacion.set(self.final_seleccionado[5])
		self.proveedor.set(self.final_seleccionado[6])
		self.fecha_actual = self.final_seleccionado[7]
		self.cant_caja.set(self.final_seleccionado[8])
		self.cant_uni.set(self.final_seleccionado[9])
		self.prec_caja.set(self.final_seleccionado[10])
		self.calcPrecxUnd.set(self.final_seleccionado[11])
		self.prec_venta_caja.set(self.final_seleccionado[12])
		self.prec_venta_uni.set(self.final_seleccionado[13])
		
		
	def buscar_item_nombre_fun(self):
		for i in self.tv_result_mod_item.get_children():
			self.tv_result_mod_item.delete(i)
		self.item = db_item_manager_class()
		consulta = self.item.buscar_item_nombre(self.nombre_buscar.get())
		for i in range (len(consulta)):
			j = consulta[i]
			self.tv_result_mod_item.insert("", END, values = (str(j[0]), str(j[1])))
			
			
	def buscar_item_codigo_fun(self):
		for i in self.tv_result_mod_item.get_children():
			self.tv_result_mod_item.delete(i)
		self.item = db_item_manager_class()
		consulta = self.item.buscar_item_codigo(self.nombre_buscar.get())
		for i in range (len(consulta)):
			j = consulta[i]
			self.tv_result_mod_item.insert("", END, values = (str(j[0]), str(j[1])))
		#self.tv_result_mod_item.insert("", END, self.item.buscar_item_nombre(self.nombre_buscar.get()))
		
		
		
		
	########### FRAME BUSCAR ITEM ####=
	
	def crear_frm_buscar_item(self):
		self.frm_almacen.place_forget()
		
		self.frm_buscar_item = Frame(self.root, height = 2000, width = 1500, bg = "#ADD8E6")
		self.frm_buscar_item.place(x = 0, y = 300)
		
		self.entry_busqueda_item = Entry(self.frm_buscar_item, textvariable = self.nombre_buscar)
		self.entry_busqueda_item.place(x = 100, y = 100, height = 100)
		
		self.lbl_buscar_item = Label(self.frm_buscar_item, text = "BUSCAR POR:", bg = "skyblue")
		self.lbl_buscar_item.place(x = 100, y = 250)
		
		self.btn_buscar_cod_item_busc = Button(self.frm_buscar_item, text = "Código", command = lambda : self.buscar_item_codigo_fun_buscar())
		self.btn_buscar_cod_item_busc.place(x = 80, y = 350)
		
		self.btn_buscar_nom_item_busc = Button(self.frm_buscar_item, text = "Nombre", command = lambda : self.buscar_item_nombre_fun_buscar())
		self.btn_buscar_nom_item_busc.place(x = 400, y = 350)
		
		
		
		
		#### Treeview ####
		
		self.tv_result_buscar_item = ttk.Treeview(self.frm_buscar_item, columns = 3)
		self.tv_result_buscar_item.place(x = 100, y = 800, width = 1200)
		self.tv_result_buscar_item['columns'] = ('COD_INT',  'DESCRIPCION')
		
		self.s = ttk.Style()
		self.s.theme_use('clam')
		
		self.s.configure('Treeview', rowheight = 90)
		
		self.tv_result_buscar_item.column('#0', width = 0, stretch = 0)
		self.tv_result_buscar_item.column('COD_INT', anchor = CENTER, stretch = 0, width = 250)
		self.tv_result_buscar_item.column('DESCRIPCION', anchor = CENTER, width = 10)
		
		
		
		
		self.tv_result_buscar_item.heading('#0', text=' ', anchor=CENTER)
		self.tv_result_buscar_item.heading('COD_INT', text='CÓDIGO.', anchor=CENTER)

		self.tv_result_buscar_item.heading('DESCRIPCION', text='DESCRIPCION',anchor=CENTER)
		
		self.btn_tv = Button(self.frm_buscar_item, text = "Select", command = lambda : self.select_row_consulta())
		self.btn_tv.place( x = 300, y = 1800)
		
		
		
	def buscar_item_nombre_fun_buscar(self):
		for i in self.tv_result_buscar_item.get_children():
			self.tv_result_buscar_item.delete(i)
		self.item = db_item_manager_class()
		consulta = self.item.buscar_item_nombre(self.nombre_buscar.get())
		for i in range (len(consulta)):
			j = consulta[i]
			self.tv_result_buscar_item.insert("", END, values = (str(j[0]), str(j[1])))
			
			
	def buscar_item_codigo_fun_buscar(self):
		for i in self.tv_result_buscar_item.get_children():
			self.tv_result_buscar_item.delete(i)
		self.item = db_item_manager_class()
		consulta = self.item.buscar_item_codigo(self.nombre_buscar.get())
		for i in range (len(consulta)):
			j = consulta[i]
			self.tv_result_buscar_item.insert("", END, values = (str(j[0]), str(j[1])))
			
			
	def crear_frm_tabla_consulta_item(self):
		self.nombre_consulta = StringVar()
		self.descripcion_consulta = StringVar()
		self.stock_consulta = StringVar()
		self.presentacion_consulta = StringVar()
		self.proveedor_consulta = StringVar()
		self.fecha_ult_mod_consulta = StringVar()
		self.frm_buscar_item.place_forget()
		self.estilo = tkFont.Font(family = "Arial", size = 10)
		self.frm_consulta = Frame(self.root, bg = "blue", height = 2900, width = 2000)
		self.frm_consulta.place(x=0, y= 0)
			
		self.lbl_nombre_consulta = Label(self.frm_consulta, textvariable = self.nombre_consulta, font = self.estilo, bg = "pink")
		self.lbl_nombre_consulta.place(x = 100, y = 300, height= 130)
		
		self.lbl_descripcion_consulta = Label(self.frm_consulta, textvariable = self.descripcion_consulta, anchor = 'nw', font = tkFont.Font(family = " Arial", size = 8), bg = "pink")
		self.lbl_descripcion_consulta.place(x = 100, y = 500, height= 150)
		
		self.lbl_cantidad_stock = Label(self.frm_consulta, textvariable = self.stock_consulta, font = tkFont.Font(family = " Arial", size = 8), bg = "pink")
		self.lbl_cantidad_stock.place(x = 100, y = 700, height= 100)
			
		self.lbl_presentacion_consulta = Label(self.frm_consulta, textvariable = self.presentacion_consulta, font = tkFont.Font(family = " Arial", size = 8), bg = "pink")	
		self.lbl_presentacion_consulta.place(x = 100, y = 850, height= 100)
			
		self.lbl_proveedor_consulta = Label(self.frm_consulta, textvariable = self.proveedor_consulta, font = tkFont.Font(family = " Arial", size = 8), bg = "pink")
		self.lbl_proveedor_consulta.place(x = 100, y = 1000, height= 100)
		
		
		self.lbl_fecha_ult_mod_consulta = Label(self.frm_consulta, textvariable = self.fecha_ult_mod_consulta, font = tkFont.Font(family = " Arial", size = 8), bg = "pink")
		self.lbl_fecha_ult_mod_consulta.place(x = 100, y = 1150, height= 100)
		
		
		
	def select_row_consulta(self):
		self.crear_frm_tabla_consulta_item()
		self.item = db_item_manager_class()
		
		self.selected = self.tv_result_buscar_item.item(self.tv_result_buscar_item.focus())['values']
		
		self.final_seleccionado = self.item.set_inputs_frame_modificador(self.selected[0])
		self.final_seleccionado = self.final_seleccionado[0]
		
		
		#nombre_consulta = StringVar()
#		self.descripcion_consulta = StringVar()
#		self.stock_consulta = StringVar()
#		self.presentacion_consulta = StringVar()
#		self.proveedor_consulta = StringVar()
#		self.fecha_ult_mod_con
		
		self.nombre_consulta.set(self.final_seleccionado[3])
		self.descripcion_consulta.set(self.final_seleccionado[4])
		self.stock_consulta.set(f"STOCK DISPONIBLE: {self.final_seleccionado[8]}")
		self.presentacion_consulta.set(f"PRESENTACIÓN: {self.final_seleccionado[5]}")
		self.proveedor_consulta.set(self.final_seleccionado[6])
		self.fecha_ult_mod_consulta.set(self.final_seleccionado[7])
		
#########MENU PRINCIPAL###########
		
		
class MenuPrincipal():
	
	def __init__(self, root, responsable, gate, admin):
		self.root = root
		self.responsable_mp = responsable
		self.gate_mp = gate
		self.admin_mp = admin
	
	def crear_frame_principal_menu(self):
		self.frame_principal = Frame(self.root, bg = "#ADD8E6", width = 900, height = 2000)
		self.frame_principal.place(x = 0, y = 0)
		#UsersClass(padre).borra_inicio_sesion()
		
		
		####Botones#####
		
		self.btn_almacen_menu_principal = Button(self.frame_principal, width = 15, height = 3, text = "ALMACEN", command = lambda : [AlmacenClass(self.root, self.responsable_mp). crear_frame_almacen(), self.frame_principal.place_forget()])
		self.btn_almacen_menu_principal.place(x = 100, y = 100)
		
		
		
		self.btn_facturacion_menu_principal = Button(self.frame_principal, width = 15, height = 3,text = "FACTURACIÓN", command = lambda : [Facturacion(self.root, self.responsable_mp).crear_frame_facturacion(), self.frame_principal.place_forget()])
		self.btn_facturacion_menu_principal.place(x = 100, y = 390)
		
		
		
		
		self.btn_usuario_menu_principal = Button(self.frame_principal, width = 15, height = 3, text = "USUARIO", command = lambda : [UsersClass(self.root).crear_frame_menu_usuario(self.gate_mp, self.admin_mp), self.frame_principal.place_forget()])
		self.btn_usuario_menu_principal.place(x = 100, y = 680)
	
	
	
	
class Facturacion():
	
	
	
	def __init__(self, root, responsable):
		self.padre = root
		self.responsable_fact = responsable
		
		
	def crear_frame_facturacion(self):
		
		self.frm_facturacion_menu = Frame(self.padre, width = 850, height = 1500, bg = "#778899")
		self.frm_facturacion_menu.place(x = 10, y = 100)
		
		self.lbl_facturacion_menu= Label(self.frm_facturacion_menu, text = "Factura", bg = "skyblue", width = 15, height = 1, font = ("Arial", 10))
		self.lbl_facturacion_menu.place(x = 50, y = 100)
		
		
		
		self.btn_generar_factura = Button(self.frm_facturacion_menu, text = "Generar factura", bg = "#DCDCDC", width = 10)
		self.btn_generar_factura.place(x = 50, y = 250)
		
		
		
		self.btn_eliminar_factura = Button(self.frm_facturacion_menu, text = "Eliminar factura", bg = "#DCDCDC", width = 10)
		self.btn_eliminar_factura.place(x = 50, y = 400)
		
		self.lbl_eliminar_fact_admin_needed = Label(self.frm_facturacion_menu, text = '(Administrador)', bg = "red")
		self.lbl_eliminar_fact_admin_needed.place(x = 480, y = 420)
		
		
		
		self.btn_revisar_factura = Button(self.frm_facturacion_menu, text = "Revisar factura", bg = "#DCDCDC", width = 10)
		self.btn_revisar_factura.place(x = 50, y = 550)
		
		
		self.btn_volver = Button(self.frm_facturacion_menu, text = "Volver", command = lambda : [self.frm_facturacion_menu.place_forget(), MenuPrincipal(self.padre, self.responsable_fact, UsersClass.gate_user, UsersClass.puerta_admin).crear_frame_principal_menu()])
		self.btn_volver.place(x = 200, y = 1200)
	
	
#class Conector():
#	
#	def __init__(self, padre):
#				
#		self.main_window = padre
#		self.user_gate_con = False
#		u = UsersClass(self.main_window)
#		self.btn_inicio_sesion = Button(self.main_window, text = "INICIO DE SESIÓN", command = lambda : [u.frame_inicio_sesion(), self.borrar_btn()])
#		self.btn_inicio_sesion.place(x = 300, y = 300)
#		self.frame_menu_principal = Frame()
#				
#		
#	def llamar_frame_inicio_sesion(self):
#		UsersClass.frame_inicio_sesion(self.main_window)
#		self.user_gate_con = UsersClass(self.main_window).user_gate
#		
#	def llamar_frame_registro(self):
#		UsersClass.crear_frame_registro(self.main_window)
#		
#	def borrar_btn(self):
#		self.btn_inicio_sesion.place_forget()
#		
#	
#	def crear_frame_menu_principal(self):
#			UsersClass.borra_inicio_sesion(self.main_window)
#			self.frame_menu_principal = Frame(self.main_window, height = 10, width = 850, bg = "orange")
#			self.frame_menu_principal.place(x = 0, y = 0)
