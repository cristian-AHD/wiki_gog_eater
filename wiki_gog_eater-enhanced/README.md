# 🐉 God Eater Wiki

Wiki interactiva no oficial basada en el universo de **God Eater** y **God Eater Burst**.
Permite consultar información sobre Aragami, armas, God Eaters, áreas y materiales del juego.

## Tecnologías utilizadas

- **FastAPI** — Backend y API REST
- **SQLAlchemy** — ORM para manejo de base de datos
- **PostgreSQL (Neon)** — Base de datos en la nube
- **Pydantic** — Validación de datos
- **HTML + JavaScript** — Frontend de la wiki
- **Python 3.13**

## Modelos

- **Aragami** — Criaturas del juego con tipo, debilidades y descripción
- **Espada / Escudo / Pistola** — Partes del God Arc con stats de daño y elemento
- **Unidad de Control** — Traje del God Eater con buffs
- **God Eater** — Soldados con rango y God Arc asignado
- **Material** — Materiales obtenibles en misiones
- **Área** — Zonas del juego

## Estructura
  wiki_God_Eater/
├── mains.py        # Endpoints de la API
├── model.py        # Modelos Pydantic
├── Models_db.py    # Modelos SQLAlchemy
├── Batabase.py     # Conexión a Neon
├── static/         # Páginas HTML
│   ├── index.html
│   ├── aragami.html
│   ├── armas.html
│   ├── godeater.html
│   ├── areas.html
│   └── materiales.html
└── .env         
## ⚙️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/wiki_God_Eater.git
cd wiki_God_Eater

# Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate

# Instalar dependencias
pip install fastapi sqlalchemy psycopg2-binary python-dotenv uvicorn

# Configurar .env
DATABASE_URL=postgresql://...

# Correr el servidor
python -m fastapi dev mains.py
```

## 🌐 Endpoints principales

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /aragami | Listar aragami |
| POST | /aragami | Crear aragami |
| PUT | /aragami/{id} | Actualizar aragami |
| DELETE | /aragami/{id} | Eliminar aragami |
| GET | /espada | Listar espadas |
| GET | /godeater | Listar God Eaters |
| PUT | /imagen/{tipo}/{id} | Asignar imagen por URL |

## 📖 Documentación

Disponible en `http://127.0.0.1:8000/docs` al correr el servidor.

