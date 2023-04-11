import sqlite3

class administrador:
    def __init__(self):
        ad=int(input('consultar estados de habitaciones=1 \n consultar clientes=2 \n consultar estados de cuentas=3 \n  consultar datos de empleados=4 \n '))

    #ver estados de habitaciones 
    def ver_estado_habitaciones(self):
        conn = sqlite3.connect('Olympo.db')
        cursor = conn.cursor()
        consulta = "SELECT * FROM tb_habitaciones"
        cursor.execute(consulta)
        habitaciones = cursor.fetchall()
        print("Estado de las habitaciones:")
        for habitacion in habitaciones:
            print("Habitación:", habitacion[0], "| Estado:", habitacion[3])

    #ver todos los clientes registrados en la DB del hotel
    def ver_clientes(self):
        conn = sqlite3.connect('Olympo.db')
        cursor = conn.cursor()
        consulta = "SELECT * FROM tb_clientes"
        cursor.execute(consulta)

        clientes = cursor.fetchall()
        print("Lista de clientes:")
        for cliente in clientes:
            print("ID:", cliente[0], "| Nombre:", cliente[1], "| Apellido:", cliente[2], "| Teléfono:", cliente[3])

    #ver todos los estados de cuentas de los clientes del hotel 
    def ver_cuentas_clientes(self):
        conn = sqlite3.connect('Olympo.db')
        cursor = conn.cursor()
        consulta = "SELECT * FROM tb_clientes"
        cursor.execute(consulta)
        clientes = cursor.fetchall()
        print("Cuentas de los clientes:")
        for cliente in clientes:
            print("Cliente:", cliente[0], "| Cuenta:", cliente[1])

    #ver todos los empleados del hotel 
    def ver_empleados(self):
        conn = sqlite3.connect('Olympo.db')
        cursor = conn.cursor()
        consulta = "SELECT * FROM tb_empleados"
        cursor.execute(consulta)
        empleados = cursor.fetchall()
        print("Lista de empleados:")
        for empleado in empleados:
            print("ID:", empleado[0], "| Nombre:", empleado[1], "| Apellido:", empleado[2], "| Cargo:", empleado[3])

        
#MENU
ad=administrador
a=int(input('consultar estados de todas las habitaciones=1 \n consultar clientes=2 \n consultar estados de cuentas=3 \n  consultar datos de empleados=4 \n '))
if a==1:
    ad.ver_estado_habitaciones()
elif a==2:
    ad.ver_clientes()
elif a==3:
    ad.ver_cuentas_clientes()
elif a==4:
    ad.ver_empleados()
