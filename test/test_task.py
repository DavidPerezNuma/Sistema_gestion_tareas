import unittest
from unittest.mock import patch
from src.main import main

class TestGestionTareasConsola(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        '1', 'Comprar víveres', 'Comprar frutas y verduras en el mercado',  # Agregar primera tarea
        '1', 'Terminar proyecto', 'Terminar el sistema de gestión de tareas para la universidad',  # Agregar segunda tarea
        '3',  # Ver todas las tareas
        '4', '2', 'Actualizar proyecto', 'Añadir documentación al proyecto',  # Actualizar la segunda tarea
        '3',  # Ver todas las tareas para verificar la actualización
        '2', '1',  # Eliminar primera tarea
        '3',  # Ver todas las tareas restantes
        '5'  # Salir del programa
    ])
    def test_simulacion_consola(self, mock_input):
        """
        Simula un flujo de interacción en la consola para agregar, actualizar, eliminar y ver tareas.
        """
        main()  # Ejecuta el menú principal simulando la entrada del usuario

if __name__ == "__main__":
    unittest.main()
