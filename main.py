from Cola import Cola
from Compra import Compra
from rich.console import Console
Ordenes = Cola()
Salir = False
#SE CREA EL MENU
c = Console() #Libreria para darle estilo al menú
def hacer_orden():    
    c.print("                                                 ", style="white on white")
    c.print("Ingrese el nombre del cliente                    ", style="cyan on white")
    nombre = input()
    descripcion = ""
    tiempot = 0
    orden = True
    while(orden):
        c.print("            Seleccione su ingrediente            ", style="bold cyan on white")
        c.print("1. Salchicha                                     ", style="cyan on white")
        c.print("2. Chorizo                                       ", style="cyan on white")
        c.print("3. Salami                                        ", style="cyan on white")
        c.print("4. Longaniza                                     ", style="cyan on white")
        c.print("5. Costilla                                      ", style="cyan on white")
        c.print("6. Salir                                         ", style="cyan on white")
        opcion = input("Ingrese el número de la opción que desea: ")
        if opcion == "1":
            cantidad = True
            while(cantidad):
                cant = input("Ingrese el número de shucos que desea, presione -1 para regresar: ")
                if(cant == "-1"):
                    cantidad = False
                elif(str.isdigit(cant) and int(cant) > 0):
                    cantidad = False
                    tiempot += (int(cant) * 2)
                    descripcion += str(cant) + " shucos de salchicha, "
                else:
                    c.print("Ingrese una opción válida                        ", style="red on white")
                    c.print("                                                 ", style="white on black")            
        elif opcion == "2":
            cantidad = True
            while(cantidad):
                cant = input("Ingrese el número de shucos que desea, presione -1 para regresar: ")
                if(cant == "-1"):
                    cantidad = False
                elif(str.isdigit(cant) and int(cant) > 0):
                    cantidad = False
                    tiempot += (int(cant) * 3)
                    descripcion += str(cant) + " shucos de chorizo, "
                else:
                    c.print("Ingrese una opción válida                        ", style="red on white")
                    c.print("                                                 ", style="white on black")            
        elif opcion == "3":
            cantidad = True
            while(cantidad):
                cant = input("Ingrese el número de shucos que desea, presione -1 para regresar: ")
                if(cant == "-1"):
                    cantidad = False
                elif(str.isdigit(cant) and int(cant) > 0):
                    cantidad = False
                    tiempot += (int(cant) * 1.5)
                    descripcion += str(cant) + " shucos de salami, "
                else:
                    c.print("Ingrese una opción válida                        ", style="red on white")
                    c.print("                                                 ", style="white on black")            
        elif opcion == "4":
            cantidad = True
            while(cantidad):
                cant = input("Ingrese el número de shucos que desea, presione -1 para regresar: ")
                if(cant == "-1"):
                    cantidad = False
                elif(str.isdigit(cant) and int(cant) > 0):
                    cantidad = False
                    tiempot += (int(cant) * 4)
                    descripcion += str(cant) + " shucos de longaniza, "
                else:
                    c.print("Ingrese una opción válida                        ", style="red on white")
                    c.print("                                                 ", style="white on black")
        elif opcion == "5":
            cantidad = True
            while(cantidad):
                cant = input("Ingrese el número de shucos que desea, presione -1 para regresar: ")
                if(cant == "-1"):
                    cantidad = False
                elif(str.isdigit(cant) and int(cant) > 0):
                    cantidad = False
                    tiempot += (int(cant) * 6)
                    descripcion += str(cant) + " shucos de costilla, "
                else:
                    c.print("Ingrese una opción válida                        ", style="red on white")
                    c.print("                                                 ", style="white on black")         
        elif opcion == "6":
            orden = False
        else:
            c.print("Ingrese una opción válida                        ", style="red on white")
            c.print("                                                 ", style="white on white")
    if(tiempot > 0):
            compra = Compra(nombre, descripcion, tiempot)
            Ordenes.insertar(compra)
            c.print("Orden Finalizada correctamente, tiempo a esperar: " + Ordenes.get_tiempoespera() + " min", style="red on white")
            input("Introduzca cualquier letra para continuar: ")
        

    
while (Salir == False):
    c.print("*************************************************", style="black on white")
    c.print("                SHUCOS LOS CHATOS                ", style="bold cyan on white")    
    c.print("0. Ver los datos del desarrollador               ", style="cyan on white")
    c.print("1. Ingresar una orden nueva                      ", style="cyan on white")
    c.print("2. Despachar orden                               ", style="cyan on white")
    c.print("3. Ver ordenes pendientes                        ", style="cyan on white")
    c.print("4. Salir                                         ", style="cyan on white")
    c.print("                                                 ", style="cyan on white")
    c.print("*************************************************", style="black on white")
    opcion = input("Ingrese el número de la opción que desea: ")
    if opcion == "0":
        c.print("*************************************************", style="white on black")
        c.print("Nombre: José David Panaza Batres                 ", style="white on black")
        c.print("Carné:  202111478                                ", style="white on black")
        c.print("CUI:    3848221850101                            ", style="white on black")
        c.print("*************************************************", style="white on black")
    elif opcion == "1":
        c.print("                                                 ", style="white on black")
        c.print("*************************************************", style="black on white")
        c.print("                 INGRESAR ORDEN                  ", style="bold cyan on white")
        hacer_orden()
        Ordenes.crearReporte()
    elif opcion == "2":
        Ordenes.extraer()
        Ordenes.crearReporte()
        input("Introduzca cualquier letra para continuar: ")
    elif opcion == "3":
        Ordenes.get_ordenespendientes()
        input("Introduzca cualquier letra para continuar: ")
    elif opcion == "4":
        Salir = True
        c.print("Vuelva pronto!", style="bold underline white on black")
    else:
        c.print("Ingrese una opción válida                        ", style="red on white")
        c.print("                                                 ", style="white on black")


