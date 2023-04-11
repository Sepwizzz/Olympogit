import sqlite3
class recepcionista:
    def __init__(self):
        r=int(input('consultar estado de habitacion=1 \n cambiar estado de habitacion=2 \n consultar estado de cuenta de cliente=3 \n generar factura=4 '))

    #funcion para ver el estado de habitacion en el rol recepcionista
    def Con_estado_habitacion(self, id_habitacion):
        conn = sqlite3.connect('Olympo.db')
        cursor = conn.cursor()

        consulta = "SELECT estado FROM tb_habitaciones WHERE numero=?"
        cursor.execute(consulta, (id_habitacion,))
        resultado = cursor.fetchone()
        if resultado:
            print("Estado de la habitación", id_habitacion, ":", resultado[0])
        else:
            print("La habitación", id_habitacion, "no existe")
            
    #funcion para cambiar el estado de una habitacion en el rol recepcionista 
    def cambiar_estado_habitacion(self, id_habitacion, nuevo_estado):
        conn = sqlite3.connect('Olympo.db')
        cursor = conn.cursor()

        consulta = "UPDATE tb_habitaciones SET estado=? WHERE numero=?"
        cursor.execute(consulta, (nuevo_estado, id_habitacion))

        if cursor.rowcount > 0:
            print("El estado de la habitación", id_habitacion, "se ha actualizado a", nuevo_estado)
        else:
            print("No se ha podido actualizar el estado de la habitación", id_habitacion)
        conn.commit()
    
    #funcion para consultar estados de cuentas de clientes en el rol recepcionista
    def consultar_cuentas(self, cuenta):
        conn = sqlite3.connect('Olympo.db')  
        cursor = conn.cursor()

        consulta = "SELECT * FROM tb_cuentas WHERE cuenta="
        cursor.execute(consulta, (cuenta,))
        resultados = cursor.fetchall()

        if len(resultados) > 0:
            print("Facturas para la mesa", cuenta)
            for resultado in resultados:
                print(resultado)
        else:
            print("No se encontro esta cuenta", cuenta)


    #funcion para generar facturas
    def generar_factura(self):
        return   
    
                
#MENU   
re=recepcionista
r=int(input('consultar estado de habitacion=1 \n cambiar estado de habitacion=2 \n consultar estado de cuenta de cliente=3 \n generar factura=4 '))
if r==1:
    idhab=int(input('ingrese la id de la habitacion'))
    re.Con_estado_habitacion(idhab)
elif r==2:
    idhab=int(input('ingrese el id de la habitacion'))
    nuevoEstado=input('ingrese el nuevo estado, sea disponible y/o ocupado')
    re.cambiar_estado_habitacion(idhab,nuevoEstado)
elif r==3:
    cu=input('ingrese la id de cuenta del cliente')
    re.consultar_cuentas(cu)
elif r==4:
    re.generar_factura
    