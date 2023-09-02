from src.config import Config
import csv


class App:
    def __init__(self):
        self.config = Config()

    def run(self) -> None:
        """run application

        Aquí es donde debe implementarse la lógica de funcionamiento
        de la aplicación; donde se llamarán las clases Screen, ConsoleInteract
        en bucle permanente(a menos que el usuario decida salir)

        """
        print("The app is running")
        print(self.config.data_path)

    def datapath(self, path: str) -> None:
        """Method that change the datapath configuration.

        Args:
            path (str): relative path from migra.py
        """
        self.config.set_datapath(path)


# CSV Sample code
# import csv


# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad


# personas = []
# with open("file.csv", "r") as file:
#     reader = csv.reader(file)
#     next(reader)  # Saltar la primera fila si tiene encabezados
#     for row in reader:
#         nombre, apellido, edad = row
#         persona = Persona(nombre, apellido, int(edad))
#         personas.append(persona)
