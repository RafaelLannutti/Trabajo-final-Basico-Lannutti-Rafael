import pickle, sys, os, random

def menu():
    
    print("         Bienvenido al Sistema de Tickets")
    print("1. Generar un Nuevo Ticket")
    print("2. Leer un Ticket")
    print("3. Salir")

def crear_ticket():
    os.system("cls")
    numero_ticket = random.randrange(1000, 9999)
    print("Ingrese los datos para generar un nuevo ticket")
    nombre = input("Ingrese su Nombre: ")
    sector = input("Ingrese su Sector: ")
    asunto = input("Ingrese Asunto: ")
    mensaje = input("Ingrese un Mensaje: ")
    ticket_dicc = {
        
        "ticket" : numero_ticket ,
        "nombre" : nombre ,
        "sector" : sector ,
        "asunto" : asunto ,
        "mensaje": mensaje ,
    }
    nombre_archivo = f"ticket_{numero_ticket}.txt"
    with open(nombre_archivo, "wb") as f:
        pickle.dump(ticket_dicc, f)
    os.system("cls")
    # print(ticket_dicc)
    for clave,valor in ticket_dicc.items():
        print(f"{clave},{valor}")
    print(f"Su ticket es: {numero_ticket}, IMPORTANTE, por favor no olvidar")
    return ticket_dicc, numero_ticket

   
def leer_ticket():
    os.system("cls")
    ticket_numero = input("Ingrese el número del ticket a leer: ")
    nombre_archivo = f"ticket_{ticket_numero}.txt"

    try:
        with open(nombre_archivo, "rb") as f:
            ticket_data = pickle.load(f)

        print("Datos del ticket:")
        for clave, valor in ticket_data.items():
            print(f"{clave.capitalize()}: {valor}")
        
    except FileNotFoundError:
        print("Error: No se encontró el ticket con ese número.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")    


def main():
    for archivo in os.listdir():        
        if archivo.endswith(".txt"):
            os.remove(archivo)
    os.system("cls")
    while True:
        menu()
        choice = input("Seleccione una opción: ")
        if choice == '1':
            crear_ticket()
            
            
            while True:                
                pregunta = input("¿Desea crear otro ticket? (si/no): ").lower()

                if pregunta == "si":
                    os.system("cls")
                    ticket_info = crear_ticket()                   
                elif pregunta == "no":
                    break
                else:
                    print("Opción inválida. Ingrese 'si' o 'no'.")
            input("Presione enter para continuar")
            os.system("cls")
        elif choice == '2':
            leer_ticket()
            input("Presione enter para continuar")
            os.system("cls")
            while True:                
                pregunta = input("¿Desea leer otro ticket? (si/no): ").lower()

                if pregunta == "si":
                    os.system("cls")
                    leer_ticket()                  
                elif pregunta == "no":
                    os.system("cls")
                    break
                else:
                    print("Opción inválida. Ingrese 'si' o 'no'.")
            
        elif choice == '3':
            os.system("cls")
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            input("Presione enter para continuar")
            os.system("cls")

if __name__ == "__main__":
    main()
