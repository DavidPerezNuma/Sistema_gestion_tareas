from src.task import agregar_tarea, eliminar_tarea, ver_tareas, marcar_completada

def mostrar_menu():
    """
    Función que imprime el menú principal con las opciones disponibles.
    """
    print("\n--- Menú de Gestión de Tareas ---")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Ver todas las tareas")
    print("4. Marcar tarea como completada")
    print("5. Salir")
    
def ejecutar_opcion(opcion, lista_tareas):
    """
    Función que ejecuta la acción correspondiente a la opción elegida por el usuario.
    Args:
        opcion (int): La opción elegida del menú.
        lista_tareas (list): Lista que contiene todas las tareas.
    """
    if opcion == 1:
        agregar_tarea(lista_tareas)
    elif opcion == 2:
        eliminar_tarea(lista_tareas)
    elif opcion == 3:
        ver_tareas(lista_tareas)
    elif opcion == 4:
        marcar_completada(lista_tareas)
    elif opcion == 5:
        print("Saliendo del programa...")
        return False
    else:
        print("Opción no válida. Intenta de nuevo.")
    return True

def main():
    """
    Función principal que mantiene el ciclo del menú hasta que el usuario elige salir.
    """
    lista_tareas = []  # Lista para almacenar las tareas
    continuar = True
    while continuar:
        mostrar_menu()
        try:
            opcion = int(input("Elige una opción (1-5): "))
            continuar = ejecutar_opcion(opcion, lista_tareas)
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
