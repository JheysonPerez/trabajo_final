import os
import sys
from flask import Flask, render_template, request, redirect, url_for
from infrastructure.database import get_db
from infrastructure.models import Cliente

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Configurar la ruta para las carpetas de templates y static
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates')
app = Flask(__name__, static_folder='../static', template_folder=template_dir)

@app.route('/')
def home():
    return redirect(url_for('vista_clientes'))

@app.route('/vista_clientes')
def vista_clientes():
    return render_template('vista_clientes.html')

@app.route('/vista_usuario')
def vista_usuario():
    # Aquí podrías obtener el historial real de compras desde la base de datos
    historial = [
        {'fecha_registro': '2024-10-01', 'descripcion': 'Producto A', 'valor_estimado': 100, 'estado': 'Nuevo'},
        {'fecha_registro': '2024-10-02', 'descripcion': 'Producto B', 'valor_estimado': 200, 'estado': 'Usado'},
    ]
    return render_template('vista_usuario.html', historial=historial)

@app.route('/clientes', methods=['POST'])
def add_cliente():
    try:
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        email = request.form['email']
        telefono = request.form['telefono']
        
        nuevo_cliente = Cliente(nombre=nombre, apellidos=apellidos, email=email, telefono=telefono)
        
        db = next(get_db())
        db.add(nuevo_cliente)
        db.commit()
        
        return redirect(url_for('show_data'))
    except Exception as e:
        print(f"Error al agregar cliente: {e}")
        return "Ocurrió un error al agregar el cliente.", 500

@app.route('/show_data')
def show_data():
    try:
        db = next(get_db())
        clientes = db.query(Cliente).all()
        return render_template('show_data.html', clientes=clientes)
    except Exception as e:
        print(f"Error al obtener clientes: {e}")
        return "Ocurrió un error al mostrar los datos de clientes.", 500

if __name__ == "__main__":
    app.run(debug=True)
