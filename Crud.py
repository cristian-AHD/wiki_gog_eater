import csv
import os
import json


class CRUDCSV:

    def __init__(self, archivo):
        self.archivo = archivo
        self._datos = []

        if os.path.exists(archivo) and os.path.getsize(archivo) > 0:
            with open(archivo, newline="", encoding="utf-8") as f:
                self._datos = list(csv.DictReader(f))

    def _guardar(self):
        if not self._datos:
            return
        with open(self.archivo, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self._datos[0].keys())
            writer.writeheader()
            writer.writerows(self._datos)

    def _a_dict(self, item):
        if not hasattr(item, "model_dump"):
            return item
        return {
            k: (json.dumps(v) if isinstance(v, list) else ("" if v is None else getattr(v, "value", v)))
            for k, v in item.model_dump().items()
        }

    def __len__(self):      return len(self._datos)
    def __iter__(self):     return iter(self._datos)
    def __getitem__(self, i): return self._datos[i]

    def __setitem__(self, i, value):
        self._datos[i] = self._a_dict(value)
        self._guardar()

    def append(self, item):
        fila = self._a_dict(item)
        self._datos.append(fila)
        self._guardar()

    def save(self):
        self._guardar()
