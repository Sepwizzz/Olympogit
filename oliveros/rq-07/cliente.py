import sqlite3

class Cliente:
    def __init__(self):
        None
        
    #ver habitaciones en el rol cliente
    def ver_habitaciones(self):
        conn = sqlite3.connect('olympo.db')
        cursor = conn.cursor()
        consulta = "SELECT * FROM tb_habitaciones"
        cursor.execute(consulta)

        habitaciones = cursor.fetchall()
        print("Lista de habitaciones:")
        for habitacion in habitaciones:
            print("ID:", habitacion[0], "| Tipo:", habitacion[1], "| Descripción:", habitacion[2], "| Precio:", habitacion[3])

    #ver servicios del hotel
    def ver_servicios(self):
        conn = sqlite3.connect('olympo.db')
        cursor = conn.cursor()

        consulta = "SELECT * FROM tb_servicios"
        cursor.execute(consulta)
        servicios = cursor.fetchall()
        print("Lista de servicios:")
        for servicio in servicios:
            print("ID:", servicio[0], "| Nombre:", servicio[1], "| Descripción:", servicio[2], "| Precio:", servicio[3])

    #realizar una reserva como cliente
    def Reservar(self, tipo_habitacion, cantidad_personas, fecha_inicio, fecha_fin):
 
        conn = sqlite3.connect('Olympo.db')
        cursor = conn.cursor()

        consulta = "SELECT * FROM tb_habitaciones WHERE tipo = ? AND capacidad >= ?"
        cursor.execute(consulta, (tipo_habitacion, cantidad_personas))
        habitaciones = cursor.fetchall()

        disponible = False
        for habitacion in habitaciones:
            consulta = "SELECT * FROM tb_reservas WHERE id_habitacion = ? AND ((fecha_inicio BETWEEN ? AND ?) OR (fecha_fin BETWEEN ? AND ?))"
            cursor.execute(consulta, (habitacion[0], fecha_inicio, fecha_fin, fecha_inicio, fecha_fin))
            reservas = cursor.fetchall()
            if not reservas:
                disponible = True
                habitacion_id = habitacion[0]
                break
        if disponible:
            consulta = "INSERT INTO tb_reservas (id_habitacion, cantidad_personas, fecha_inicio, fecha_fin) VALUES (?, ?, ?, ?)"
            cursor.execute(consulta, (habitacion_id, cantidad_personas, fecha_inicio, fecha_fin))
            conn.commit()
            print("¡Reserva realizada con éxito!")
        else:
            print("Lo siento, no hay habitaciones disponibles para las fechas seleccionadas.")




#MENU
cl=Cliente
c=int(input('ver habitaciones del hotel=1 \n  consultar servicios del hotel=2 \n realizar una reserva=3 \n '))
if c==1:
    cl.ver_habitaciones()
elif c==2:
    cl.ver_habitaciones()
elif c==3:
    tp=input('ingrese el tipo de habitacion')
    can=int(input('ingrese la cantidad de personas a hospedarse'))
    ini=input('ingrese la fecha de inicio de la reserva')
    fin=input('ingrese la fecha de fin de la reserva')
    cl.Reservar(tp,can,ini,fin)