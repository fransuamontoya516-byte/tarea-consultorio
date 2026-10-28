from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración de conexión a la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',       # Cambia si tu usuario de MySQL es distinto
    'password': '',       # Agrega tu contraseña si la tienes
    'database': 'Consultorio'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# ==========================================
# RUTAS PARA PACIENTES (CRUD)
# ==========================================

@app.route('/pacientes', methods=['GET'])
def get_pacientes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pacientes")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result), 200

@app.route('/pacientes', methods=['POST'])
def create_paciente():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO pacientes (DNI, NOMBRE, APELLIDO, FECHA_DE_NACIMIENTO, CELULAR) VALUES (%s, %s, %s, %s, %s)"
    values = (data['DNI'], data['NOMBRE'], data['APELLIDO'], data['FECHA_DE_NACIMIENTO'], data['CELULAR'])
    cursor.execute(sql, values)
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify({"message": "Paciente creado exitosamente", "id": new_id}), 201

@app.route('/pacientes/<int:id>', methods=['PUT'])
def update_paciente(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE pacientes SET DNI=%s, NOMBRE=%s, APELLIDO=%s, FECHA_DE_NACIMIENTO=%s, CELULAR=%s WHERE ID=%s"
    values = (data['DNI'], data['NOMBRE'], data['APELLIDO'], data['FECHA_DE_NACIMIENTO'], data['CELULAR'], id)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Paciente actualizado exitosamente"}), 200

@app.route('/pacientes/<int:id>', methods=['DELETE'])
def delete_paciente(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pacientes WHERE ID = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Paciente eliminado exitosamente"}), 200

# ==========================================
# RUTAS PARA CITAS (CRUD)
# ==========================================

@app.route('/citas', methods=['GET'])
def get_citas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM citas")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result), 200

@app.route('/citas', methods=['POST'])
def create_cita():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO citas (ID_PACIENTE, FECHA, HORA, PRE_DIAGNOSTICO, ESTADO) VALUES (%s, %s, %s, %s, %s)"
    values = (data['ID_PACIENTE'], data['FECHA'], data['HORA'], data['PRE_DIAGNOSTICO'], data['ESTADO'])
    cursor.execute(sql, values)
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify({"message": "Cita creada exitosamente", "id": new_id}), 201

@app.route('/citas/<int:id>', methods=['PUT'])
def update_cita(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE citas SET ID_PACIENTE=%s, FECHA=%s, HORA=%s, PRE_DIAGNOSTICO=%s, ESTADO=%s WHERE ID=%s"
    values = (data['ID_PACIENTE'], data['FECHA'], data['HORA'], data['PRE_DIAGNOSTICO'], data['ESTADO'], id)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Cita actualizada exitosamente"}), 200

@app.route('/citas/<int:id>', methods=['DELETE'])
def delete_cita(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM citas WHERE ID = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Cita eliminada exitosamente"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)