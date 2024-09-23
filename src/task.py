def agregar_tarea(lista_tareas):
    """
    Función para agregar una nueva tarea a la lista.
    Args:
        lista_tareas (list): La lista donde se almacenan todas las tareas.
    """
    titulo = input("Título de la tarea: ")
    descripcion = input("Descripción de la tarea: ")
    tarea = {"titulo": titulo, "descripcion": descripcion, "estado": "Pendiente"}
    lista_tareas.append(tarea)
    print(f"Tarea '{titulo}' agregada correctamente.")

def eliminar_tarea(lista_tareas):
    """
    Función para eliminar una tarea existente de la lista.
    Args:
        lista_tareas (list): La lista que contiene todas las tareas.
    """
    ver_tareas(lista_tareas)  # Mostrar las tareas antes de eliminar
    try:
        indice = int(input("Elige el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(lista_tareas):
            tarea_eliminada = lista_tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada['titulo']}' eliminada correctamente.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def ver_tareas(lista_tareas):
    """
    Función para ver todas las tareas con su estado actual.
    Args:
        lista_tareas (list): La lista que contiene todas las tareas.
    """
    if not lista_tareas:
        print("No hay tareas para mostrar.")
        return
    print("\n--- Lista de Tareas ---")
    for idx, tarea in enumerate(lista_tareas, start=1):
        print(f"{idx}. {tarea['titulo']} - {tarea['descripcion']} [{tarea['estado']}]")

def marcar_completada(lista_tareas):
    """
    Función para marcar una tarea como completada.
    Args:
        lista_tareas (list): La lista que contiene todas las tareas.
    """
    ver_tareas(lista_tareas)  # Mostrar las tareas antes de marcar como completada
    try:
        indice = int(input("Elige el número de la tarea a marcar como completada: ")) - 1
        if 0 <= indice < len(lista_tareas):
            lista_tareas[indice]['estado'] = "Completada"
            print(f"Tarea '{lista_tareas[indice]['titulo']}' marcada como completada.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
