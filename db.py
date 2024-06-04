import pyodbc

connection_string = (
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=JAVIER\SQLEXPRESS;'
    'DATABASE=prueba;'
    "Trusted_Connection=yes;" #Para login de microsoft
    "Encrypt=no;"  # Esta opción desactiva el uso de SSL
    "TrustServerCertificate=yes;"
)
#funcion para hacer la conexion, con los datos
def get_connection():
    return pyodbc.connect(connection_string)