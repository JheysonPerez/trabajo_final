from .database import Base, engine
from .models import Cliente, FormaPago, Transaccion, TipoTransaccion, Articulo, EstadoArticulo

def main():
    # Crea las tablas
    Base.metadata.create_all(engine)
    print("Tablas creadas correctamente.")

if __name__ == "__main__":
    main()
    
from .database import Base, engine
from .models import Cliente, FormaPago, Transaccion, TipoTransaccion, Articulo, EstadoArticulo

def main():
    # Crea las tablas
    Base.metadata.create_all(engine)
    print("Tablas creadas correctamente.")

if __name__ == "__main__":
    main()

