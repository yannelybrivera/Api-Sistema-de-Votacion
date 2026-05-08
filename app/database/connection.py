import pyodbc

try:
    conexion = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost;'
        'DATABASE=SISTEMA_VOTACION;'
        'Trusted_Connection=yes;'
    )

    print("Conexión exitosa")

except Exception as e:
    print("Error de conexión")
    print(e)