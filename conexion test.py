# conexion test.py
import pyodbc
import db


try:
    conn = pyodbc.connect(db.connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT 1')
    row = cursor.fetchone()
    print("Conexión exitosa:", row)
    conn.close()
except pyodbc.Error as e:
    print("Error al conectar a la base de datos:", e)