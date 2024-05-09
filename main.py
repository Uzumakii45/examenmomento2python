def recibir_datos():
    ciclistas = []
    codigos = []  
    print("Introduce los datos de los ciclistas o escribe 'menu' para finalizar la entrada de datos y acceder al menú.")
    while True:
        codigo = input("Ingresa el código del ciclista\n** Ingresa el código para registrar **\n** 'Menu' para mostrar datos **\n** 'Terminar' para finalizar **\n")
        if codigo.lower() == 'menu':
            break
        if codigo.lower() == 'terminar':
            print("Finalizando el programa.")
            return ciclistas
        if codigo in codigos:  
            print("Error: El código ya fue ingresado previamente.")
            continue
        nombre = input("Ingresa el nombre del ciclista: ")
        edad = input("Ingresa la edad del ciclista: ")
        pais = input("Ingresa el país del ciclista: ")
        equipo = input("Ingresa el equipo del ciclista: ")
        tiempo = float(input("Ingresa el tiempo (en minutos) de la última prueba: "))
        ciclistas.append((codigo, nombre, edad, pais, equipo, tiempo))
        codigos.append(codigo)  
    return ciclistas


def mostrar_tiempos(ciclistas):
    print("Todos los tiempos registrados:")
    for ciclista in ciclistas:
        print(f"Código: {ciclista[0]}, Tiempo: {ciclista[5]} min")


def mostrar_tabla(ciclistas):
    print("Tabla de Posiciones:")
    for ciclista in sorted(ciclistas, key=lambda x: x[5]):  
        print(f"Código: {ciclista[0]}, Nombre: {ciclista[1]}, Edad: {ciclista[2]}, País: {ciclista[3]}, Equipo: {ciclista[4]}, Tiempo: {ciclista[5]} min")


def corregir_tiempo(ciclistas, codigo, nuevo_tiempo):
    for i in range(len(ciclistas)):
        if ciclistas[i][0] == codigo:
            ciclistas[i] = ciclistas[i][:5] + (nuevo_tiempo,)
            print("Tiempo actualizado correctamente.")
            return
    print("Error: El código ingresado no corresponde a un ciclista registrado.")


def retirar_ciclista(ciclistas, codigo):
    for i in range(len(ciclistas)):
        if ciclistas[i][0] == codigo:
            del ciclistas[i]
            print("Ciclista retirado correctamente.")
            return
    print("Error: El código ingresado no corresponde a un ciclista registrado.")


def main():
    ciclistas = recibir_datos()
    while True:
        accion = input("¿Qué deseas hacer? (mostrar, mostrar tiempos, corregir, retirar, salir): ")
        if accion.lower() == 'mostrar':
            mostrar_tabla(ciclistas)
        elif accion.lower() == 'mostrar tiempos':
            mostrar_tiempos(ciclistas)
        elif accion.lower() == 'corregir':
            codigo = input("Ingresa el código del ciclista a corregir: ")
            nuevo_tiempo = float(input("Ingresa el nuevo tiempo (minutos): "))
            corregir_tiempo(ciclistas, codigo, nuevo_tiempo)
        elif accion.lower() == 'retirar':
            codigo = input("Ingresa el código del ciclista a retirar: ")
            retirar_ciclista(ciclistas, codigo)
        elif accion.lower() == 'salir':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intenta nuevamente.")


main()
