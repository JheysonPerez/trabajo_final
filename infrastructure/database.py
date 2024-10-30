from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_CONNECTION = (
    "mssql+pyodbc://@ALESSANDRO\\SQLEXPRESS/PROYECTO_TIENDA?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

# Crear el motor de la base de datos
engine = create_engine(DATABASE_CONNECTION)

# Crear la base de clases de SQLAlchemy
Base = declarative_base()

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(bind=engine)

# Verificar la conexión
try:
    connection = engine.connect()
    print("Conexión establecida correctamente.")
    connection.close()
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

# Función para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
