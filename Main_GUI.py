import sqlite3 
from tkinter import *
from tkinter import messagebox
from Almacen_GUI import *
from Users_GUI import *
from pre_main import *
	

if __name__ == "__main__":
	root = Tk()
	u = UsersClass(root)
	root.config(bg ="#ADD8E6", width = 3000, height = 3000)
	#u.frame_inicio_sesion()
	
	###### Creando Menu ######
menu1 = Menu(root)
root.config(menu = menu1)

	###### Creando submenus y cascadas. ######
almacen_menu = Menu(menu1)
menu1.add_cascade(menu = almacen_menu, label = "Almacen")
almacen_menu.add_command(label = "Consultar items")
almacen_menu.add_command(label = "Buscar items")
almacen_menu.add_command(label = "Ingresar items", command = lambda : AlmacenClass(root, UsersClass.responsableFunc).crear_frame_ingreso_item())
almacen_menu.add_command(label = "Salida de items")
almacen_menu.add_command(label = "Crear nuevo items")
	
	
facturacion_menu = Menu(menu1)
menu1.add_cascade(menu = facturacion_menu, label = "Facturacion")
facturacion_menu.add_command(label = "Generar factura nueva.")
	
	
	
usuario_menu = Menu(menu1)
menu1.add_cascade(menu = usuario_menu, label = "Usuario")
usuario_menu.add_command(label = "Registrar", command = lambda : u.crear_frame_registro(UsersClass.gate_user, UsersClass.puerta_admin))
	
usuario_menu.add_command(label = "Inicio de sesión", command = lambda : u.frame_inicio_sesion())
	
usuario_menu.add_command(label = "Cerrar sesión", command = lambda : u.cerrar_sesion())
	
usuario_menu.add_command(label = "Cambiar contraseña")





root.mainloop()