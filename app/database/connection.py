import pyodbc

try:
    conexion = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost;'
        'DATABASE=SISTEMA_VOTACION;'
        'Trusted_Connection=yes;'
    )
    cursor = conexion.cursor()
    print("Conexión exitosa")

except Exception as e:
    print("Error de conexión:", e)
    raise SystemExit(1)

