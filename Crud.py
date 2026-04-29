import csv
import os

class CRUDCSV:

    def __init__(self, archivo):
        self.archivo = archivo

        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", newline="", encoding="utf-8") as file:
                pass

    def get_all(self):
        datos = []

        with open(self.archivo, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for fila in reader:
                datos.append(fila)

        return datos

    def create(self, data):

        archivo_vacio = os.path.getsize(self.archivo) == 0

        with open(self.archivo, "a", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(file, fieldnames=data.keys())

            if archivo_vacio:
                writer.writeheader()

            writer.writerow(data)

        return data
