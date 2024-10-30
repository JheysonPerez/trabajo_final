from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.database import Base
from datetime import datetime

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)  
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)  
    email = Column(String(255), unique=True, nullable=False)
    telefono = Column(String, nullable=True)

    # Relación con las transacciones
    transacciones = relationship("Transaccion", back_populates="cliente")

    # Relación con los artículos
    articulos = relationship("Articulo", back_populates="cliente")

    def __repr__(self):
        return f"<Cliente(id={self.id}, nombre='{self.nombre}', apellidos='{self.apellidos}', email='{self.email}')>"

class FormaPago(Base):
    __tablename__ = 'formas_pago'

    id = Column(Integer, primary_key=True)  # Llave primaria
    tipo = Column(String, nullable=False)  # Forma de pago (efectivo o tarjeta)

    def __repr__(self):
        return f"<FormaPago(id={self.id}, tipo='{self.tipo}')>"

class TipoTransaccion(Base):
    __tablename__ = 'tipos_transaccion'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)  # Compra, Venta

    # Relación inversa con Transaccion
    transacciones = relationship("Transaccion", back_populates="tipo")

    def __repr__(self):
        return f"<TipoTransaccion(id={self.id}, nombre='{self.nombre}')>"

class Transaccion(Base):
    __tablename__ = 'transacciones'

    id = Column(Integer, primary_key=True)  # Llave primaria
    fecha = Column(Date, default=datetime.utcnow, nullable=False)
    monto = Column(Float, nullable=False)
    tipo_id = Column(Integer, ForeignKey('tipos_transaccion.id'), nullable=False)  # Llave foránea hacia TipoTransaccion
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)  # Llave foránea hacia Cliente
    forma_pago_id = Column(Integer, ForeignKey('formas_pago.id'), nullable=False)  # Llave foránea hacia FormaPago

    # Relaciones
    tipo = relationship("TipoTransaccion", back_populates="transacciones")
    cliente = relationship("Cliente", back_populates="transacciones")  # Cambiado aquí
    forma_pago = relationship("FormaPago")  # Relación con forma de pago

    def __repr__(self):
        return f"<Transaccion(id={self.id}, fecha={self.fecha}, monto={self.monto}, tipo='{self.tipo.nombre}')>"

class Articulo(Base):
    __tablename__ = 'articulos'

    id = Column(Integer, primary_key=True)
    descripcion = Column(String, nullable=False)
    valor_estimado = Column(Float, nullable=False)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)  # Llave foránea hacia Cliente
    fecha_registro = Column(Date, default=datetime.utcnow, nullable=False)
    estado_id = Column(Integer, ForeignKey('estados_articulo.id'), nullable=False)  # Llave foránea hacia EstadoArticulo

    # Relaciones
    cliente = relationship("Cliente", back_populates="articulos")
    estado = relationship("EstadoArticulo", back_populates="articulos")

    def __repr__(self):
        return (f"<Articulo(id={self.id}, descripcion='{self.descripcion}', "
                f"valor_estimado={self.valor_estimado}, "
                f"estado='{self.estado.nombre}')>")

class EstadoArticulo(Base):
    __tablename__ = 'estados_articulo'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    # Relación con Articulo
    articulos = relationship("Articulo", back_populates="estado")

    def __repr__(self):
        return f"<EstadoArticulo(id={self.id}, nombre='{self.nombre}')>"
