"""
La empresa de eSports “eShirlitos”, necesita desarrollar un sistema 
que permita registrar los puntajes obtenidos por sus competidores en Fortnite, Valorant y Fifa. 
Para el funcionamiento del sistema se requiere las siguientes funcionalidades
1.Registrar puntajes torneo
2.Listar los todos puntajes
3.Imprimir por Tipo
4.Salir del programa
"""
competidores = []

#Menu con las opciones
def menu():
    op = 0

    while op != 4:
        print("Bienvenido, selecione su opción\n")
        print("""1.Registrar puntajes torneo.
2.Listar los todos puntajes.
3.Imprimir por Tipo.
4.Salir del programa.
""")
        try:
            op = int(input("> "))
        except:
             print("Debe ser un número.\n")

        if op == 1:
            registrar_puntaje()
        elif op == 2:
            listar_puntajes()
        elif op == 3: 
            imprimir_tipo()
        elif op == 4:
            print("Usted ha salido.")
        else:
            print("Opción no válida, intente lo denuevo.\n")

"""
1.Registrar puntajes torneo
Para registrar puntajes se requiere lo siguiente: 
Identificador de Jugador, Nombre y apellido del jugador, juego, puntaje obtenido. 
Por ejemplo, si el jugador compite en Fortnite y Fifa. 
Debe permitir seleccionar entre 1 de las 3 opciones e ingresar la cantidad de puntos obtenidos en esos dos juegos, 
también debe incluir su tipo (Principiante - Avanzado - Experto). 
Por lo tanto, un detalle de puntos del torneo podría verse registrado de la siguiente manera:"""

#Regristrar puntajes
def registrar_puntaje():

    print("Ingrese los datos requeridos")
    identificador = (input("\nIdentificador: "))
    nombre_apellido= input("Nombre y Apellido: ")
    #apellido = input("Apellido: ")

    #Un while para que los datos de los puntos sean validos
    while True:
        try:
            puntaje_valorant = int(input("Puntaje en Valorant: "))
            puntaje_fornite = int(input("Puntaje en Fornite: "))
            puntaje_fifa = int(input("Puntaje en Fifa: "))

            #Comprobacion de puntajes validos
            if puntaje_fifa < 0 or puntaje_fornite < 0 or puntaje_valorant < 0:
                print("El puntaje menor es 0.")
            else:
                break
        except:
            print("Error. \nDatos ingresados no válidos.")

    #While para comprobar que sea un tipo existente (o que piden)
    while True:
        tipo = input("Tipo (Principiante - Avanzado - Experto): ")

        if tipo.lower() == "principiante" or tipo.lower() == "avanzado" or tipo.lower() == "experto":
            break
        else:
            print("\nTipo de clase erroneo. \nPor favor, ingrese tipo nuevamente.\n")

    #Si ingresaron un dato vacío se devuelva al menú por datos imcompletos
    if not identificador or not nombre_apellido: #or not apellido:
        print("Debe ingresar todos los datos.")
        return
    
    direcctorio_judador = {
        "Identificador":identificador,
        "Nombre":nombre_apellido,
        #"Apellido":apellido,
        "Puntaje Valorant":puntaje_valorant,
        "Puntaje Fornite":puntaje_fornite,
        "Puntaje Fifa":puntaje_fifa,
        "Tipo":tipo
    }

    #Para agregar al competidor a la lista
    competidores.append(direcctorio_judador)
    print("\nRegistro exitoso.")

"""
2. Listar puntajes
Debe mostrar en la pantalla la lista de todos los puntajes registrados, similar al ejemplo anterior (opción 1)."""

def listar_puntajes():

    #Para comprobar si hay competidores
    #Si no hay se devuelve al menú con un mensaje
    if len(competidores) == 0:
        print("No se ha registrado ningún competidor aún.\n")
        return
    
    #Si hay competidores, imprimirlos
    for i in competidores:
        print(i)
    print()

"""
3.Imprimir por Tipo
Para imprimir por tipo, el usuario debe seleccionar alguno de los 3 tipos (Principiante - Avanzado - Experto). 
Estos tipos deben estar previamente definidos en algún tipo de colección de Python en el código.
Al seleccionar uno de los tipos, se generará un archivo de texto (.txt) 
con el detalle de los puntajes obtenidos por los jugadores del tipo seleccionado. 
Este debe tener la misma forma del registro completo de las opciones anteriores, pero en archivo de texto.
Cada opción de la aplicación debe desarrollarse en una función que debe llamarse desde el programa principal."""

def imprimir_tipo():

    #Para comprobar si hay competidores
    #Si no hay se devuelve al menú con un mensaje
    if len(competidores) == 0:
        print("No se ha registrado ningún competidor aún.\n")
        return
    
    #Mostrar los tipos de jugadores con los que se puede crear el .txt
    tipo = {"principiante","avanzado","experto"}
    print(f'Ingrese de que tipo de jugador quiere imprimir',",".join(tipo))

    #Un while para comprobar que se quiere crear un .txt con un tipo de jugador existente
    while True:
        tiposeleccionado = input("> ")

        if tiposeleccionado.lower() == "principiante" or tiposeleccionado.lower() == "avanzado" or tiposeleccionado.lower() == "experto":
            break
        else:
            print("\nTipo de clase erroneo. \nPor favor, ingrese tipo nuevamente.\n")

    #Se supone que es para crear el archivo 
    #print(f'Imprimir_tipo{tiposeleccionado}',",".join(tipoeleccion))
    with open(f'impresion_tipo_{tiposeleccionado}','w', encoding='utf-8') as file: #Hasta aqui esta ok
        for competidor in competidores:
            if tiposeleccionado.lower() == competidor["Tipo"]:
                file.write(f'{competidor["Identificador"]} {competidor["Nombre"]} {competidor["Puntaje Valorant"]} {competidor["Puntaje Fornite"]} {competidor["Puntaje Fifa"]}')

    print()

menu()