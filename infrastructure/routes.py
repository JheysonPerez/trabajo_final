from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from infrastructure.database import get_db
from .models import Cliente, Transaccion, Articulo, FormaPago, TipoTransaccion, EstadoArticulo

# Creación de un blueprint para las rutas
bp = Blueprint('routes_bp', __name__)

# Ruta para crear un cliente
@bp.route('/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()
    
    # Validación de datos
    if not all(key in data for key in ['nombre', 'apellidos', 'email', 'telefono']):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    nuevo_cliente = Cliente(
        nombre=data['nombre'],
        apellidos=data['apellidos'],
        email=data['email'],
        telefono=data['telefono']
    )

    db = next(get_db())
    try:
        db.add(nuevo_cliente)
        db.commit()
        return jsonify({"message": "Cliente creado exitosamente"}), 201
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()

# Ruta para crear una transacción
@bp.route('/transacciones', methods=['POST'])
def create_transaccion():
    data = request.get_json()
    
    # Validación de datos
    if not all(key in data for key in ['monto', 'tipo_id', 'cliente_id', 'forma_pago_id']):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    nueva_transaccion = Transaccion(
        fecha=data.get('fecha', datetime.utcnow()), 
        monto=data['monto'],
        tipo_id=data['tipo_id'],
        cliente_id=data['cliente_id'],
        forma_pago_id=data['forma_pago_id']
    )
    
    db = next(get_db())
    try:
        db.add(nueva_transaccion)
        db.commit()
        return jsonify({"message": "Transacción creada exitosamente"}), 201
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()

# Ruta para crear un artículo
@bp.route('/articulos', methods=['POST'])
def create_articulo():
    data = request.get_json()
    
    # Validación de datos
    if not all(key in data for key in ['descripcion', 'valor_estimado', 'cliente_id', 'estado_id']):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    nuevo_articulo = Articulo(
        descripcion=data['descripcion'],
        valor_estimado=data['valor_estimado'],
        cliente_id=data['cliente_id'],
        fecha_registro=data.get('fecha_registro', datetime.utcnow()),
        estado_id=data['estado_id']
    )
    
    db = next(get_db())
    try:
        db.add(nuevo_articulo)
        db.commit()
        return jsonify({"message": "Artículo creado exitosamente"}), 201
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()

# Ruta para crear una forma de pago
@bp.route('/formas_pago', methods=['POST'])
def create_forma_pago():
    data = request.get_json()
    
    # Validación de datos
    if 'tipo' not in data:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    nueva_forma_pago = FormaPago(
        tipo=data['tipo']
    )
    
    db = next(get_db())
    try:
        db.add(nueva_forma_pago)
        db.commit()
        return jsonify({"message": "Forma de pago creada exitosamente"}), 201
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()

# Ruta para crear un tipo de transacción
@bp.route('/tipos_transaccion', methods=['POST'])
def create_tipo_transaccion():
    data = request.get_json()
    
    # Validación de datos
    if 'nombre' not in data:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    nuevo_tipo_transaccion = TipoTransaccion(
        nombre=data['nombre']
    )
    
    db = next(get_db())
    try:
        db.add(nuevo_tipo_transaccion)
        db.commit()
        return jsonify({"message": "Tipo de transacción creado exitosamente"}), 201
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()

# Ruta para crear un estado de artículo
@bp.route('/estados_articulo', methods=['POST'])
def create_estado_articulo():
    data = request.get_json()
    
    # Validación de datos
    if 'nombre' not in data:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    nuevo_estado_articulo = EstadoArticulo(
        nombre=data['nombre']
    )
    
    db = next(get_db())
    try:
        db.add(nuevo_estado_articulo)
        db.commit()
        return jsonify({"message": "Estado de artículo creado exitosamente"}), 201
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()
