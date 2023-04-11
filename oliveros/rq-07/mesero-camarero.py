import sqlite3
class MesCam:
    def __init__(self):
        a=input('cargar a cuenta de cliente=1 \n consultar estado de cuenta de cliente=2 \n consultar estado de habitacion=3 \n ')
        
    #funcion para cargar servicio a cuenta de cliente
    def cargar_Cuenta(self,cuenta, servicio,valor):
        conexion = sqlite3.connect('Olympo.db')
        cursor = conexion.cursor()
        consulta = "INSERT INTO tb_cuenta (cuenta, servicio,valor) VALUES (#,#)"
        cursor.execute(consulta, (cuenta, servicio, valor))
        conexion.commit()

    #consultar cuentas de clientes
    def consultar_cuentas(self, cuenta):
        conn = sqlite3.connect('Olympo.db')  
        cursor = conn.cursor()
        consulta = "SELECT * FROM tb_cuenta WHERE cuenta="
        cursor.execute(consulta, (cuenta,))
        resultados = cursor.fetchall()
        if len(resultados) > 0:
            print("Facturas para la mesa", cuenta)
            for resultado in resultados:
                print(resultado)
        else:
            print("No se encontro esta cuenta", cuenta)

    #consultar estado de habitacion
    def Con_estado_habitacion(self, id_habitacion):
        conn = sqlite3.connect('Olympo.db')
        cursor = conn.cursor()
        consulta = "SELECT estadoHab FROM tb_habitaciones WHERE numero=?"
        cursor.execute(consulta, (id_habitacion,))
        resultado = cursor.fetchone()
        if resultado:
            print("Estado de la habitación", id_habitacion, ":", resultado[0])
        else:
            print("La habitación", id_habitacion, "no existe")


#MENU
meca=MesCam
a=input('cargar a cuenta de cliente=1 \n consultar estado de cuenta de cliente=2 \n consultar estado de habitacion=3 \n ')
if a==1:
    cu=int(input('ingrese la id de la cuenta del cliente'))
    ser=input('ingrese la descripcion del servicio')
    va=input('ingrese el valor del servicio')
    meca.cargar_Cuenta(cu,ser,va)
elif a==2:
    idcu=int(input('ingrese la id de cuenta del cliente'))
    meca.consultar_cuentas(idcu)
elif a==3:
    idha=input('ingrese la id de la habitacion')
    meca.Con_estado_habitacion(idha)
    
