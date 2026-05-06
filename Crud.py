import csv
import os
import json


class CRUDCSV:

    def __init__(self, archivo):
        self.archivo = archivo
        self._datos = []

        if os.path.exists(archivo) and os.path.getsize(archivo) > 0:
            with open(archivo, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    for key, value in row.items():
                        if value and value.startswith(('{', '[')):
                            try:
                                row[key] = json.loads(value)
                            except:
                                pass
                    self._datos.append(row)

    def _guardar(self):
        if not self._datos:
            if not os.path.exists(self.archivo):
                with open(self.archivo, "w", newline="", encoding="utf-8") as f:
                    pass
            return

        # Obtener fieldnames de la primera fila
        fieldnames = list(self._datos[0].keys())

        with open(self.archivo, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for row in self._datos:
                # Convertir a strings para CSV
                csv_row = {}
                for k, v in row.items():
                    if isinstance(v, (dict, list)):
                        csv_row[k] = json.dumps(v, ensure_ascii=False)
                    else:
                        csv_row[k] = v if v is not None else ""
                writer.writerow(csv_row)

    def _a_dict(self, item):
        if not hasattr(item, "model_dump"):
            return item

        data = item.model_dump()
        result = {}

        for k, v in data.items():
            if v is None:
                result[k] = ""
            elif isinstance(v, (dict, list)):
                result[k] = v
            elif hasattr(v, "value"):
                result[k] = v.value
            elif hasattr(v, "__dict__"):
                result[k] = v.model_dump() if hasattr(v, "model_dump") else str(v)
            else:
                result[k] = v

        return result

    def __len__(self):
        return len(self._datos)

    def __iter__(self):
        return iter(self._datos)

    def __getitem__(self, i):
        return self._datos[i]

    def __setitem__(self, i, value):
        self._datos[i] = self._a_dict(value)
        self._guardar()

    def append(self, item):
        fila = self._a_dict(item)
        self._datos.append(fila)
        self._guardar()

    def delete(self, indice: int):
        self._datos.pop(indice)
        self._guardar()

    def save(self):
        self._guardar()


class Historial:

    def __init__(self):
        self._historial = []

    def registrar(self, tipo: str, id_eliminado: int, nombre: str):
        self._historial.append({
            "tipo": tipo,
            "id_eliminado": id_eliminado,
            "nombre_eliminado": nombre
        })

    def obtener_todos(self):
        return self._historial.copy()

    def obtener_por_tipo(self, tipo: str):
        return [h for h in self._historial if h["tipo"] == tipo]

    def limpiar(self):
        self._historial.clear()

    def __len__(self):
        return len(self._historial)