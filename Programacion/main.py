from dispositivos import listar_dispositivos, agregar_dispositivo, buscar_dispositivo, editar_dispositivo, eliminar_dispositivo
from automatizacion import listar_automatizaciones, activar_automatizacion

def menu():
    print("\n--- Menu ---")
    print("1. Listar dispositivos")
    print("2. Buscar dispositivo")
    print("3. Agregar dispositivo")
    print("4. Editar dispositivo")
    print("5. Eliminar dispositivo")
    print("6. Ver automatizaciones")
    print("7. Activar automatización")
    print("0. Cerrar programa")


def main():
    while True:
        menu()
        opcion = input("Selecciona una opción:")

        if opcion == "1":
            dispositivos = listar_dispositivos()
            if not dispositivos: 
                print("No hay dispositivos registrados.")
            else:
                print("\n Dispositivos registrados ")
                for d in dispositivos:
                    print(f"Dispositivo ID: {d['id_dispositivo']} - {d['nombre']} ({d['tipo']}) - Estado: {d['estado']}")

        elif opcion == "2":
            nombre = input("Nombre del dispositivo a buscar:")
            dispositivo = buscar_dispositivo(nombre)
            if dispositivo:
                print(f"Dispositivo encontrado: {dispositivo}")
            else:
                print("No se encontró el dispositivo.")
        
        elif opcion == "3":
            nombre = input("Nombre del dispositivo:")
            tipo = input("Tipo de dispositivo:")
            estado = input("Estado del dispositivo (encendido/apagado):")
            nuevo_dispositivo = agregar_dispositivo(nombre, tipo, estado)
            print(nuevo_dispositivo)

        elif opcion == "4":
            nombre_original = input("Nombre del dispositivo que quieres editar:")
            dispositivo = buscar_dispositivo(nombre_original)
            print("Dejar vacíos los campos que no quieras editar.")
            nuevo_nombre = input("Nombre del dispositivo:")
            nuevo_tipo = input("Tipo de dispositivo:")
            nuevo_estado = input("Estado del dispositivo (encendido/apagado):")
            dispositivo_actualizado = editar_dispositivo(nombre_original, nuevo_nombre, nuevo_tipo, nuevo_estado)
            print(dispositivo_actualizado)
        
        elif opcion == "5":
            nombre = input("Nombre del dispositivo a eliminar:")
            dispositivo_eliminado = eliminar_dispositivo(nombre)
            if dispositivo_eliminado:
                print(f"Dispositivo eliminado: {dispositivo_eliminado}")
            else:
                print("No se encontró el dispositivo.")
        
        elif opcion == "6":
            automatizaciones = listar_automatizaciones()
            if not automatizaciones: 
                print("No existen automatizaciones.")
            else:
                print("\n Automatizaciones registradas ")
                for a in automatizaciones:
                    print(f"Automatización (ID {a['id_automatizacion']}) - Modo: {a['modo']}")

        elif opcion == "7":
            modo_automatizacion = input("Nombre modo de la automatización que quiere activar (Ingrese 'noche'):")
            automatizacion = activar_automatizacion(modo_automatizacion)
            for a in automatizacion:
                print(f"Dispositivo activado ID: {a}")

        elif opcion == "0":
            print("Se cerró el programa")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

__name__ = "__main__"
main()