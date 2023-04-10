import sqlite3


class Usuario:
    def __init__(self, nombre_usuario, apellido_usuario, id_usuario):
        self.__nombre_usuario = nombre_usuario
        self.__apellido_usuario = apellido_usuario
        self.__id_usuario = id_usuario

    def getUsuario(self):
        return "Los datos del usuario son: ",str(self.__nombre_usuario) +" "+ str(self.__apellido_usuario) +", El id del usuario  es: "+ str(self.__id_usuario)
        

class Reserva:
    def __init__(self, id_reserva, id_tipohab, habi_disp, fecha_inic, fecha_fin):
        self.__id_reserva = id_reserva
        self.__id_tipohab = id_tipohab
        self.__habi_disp = habi_disp
        self.__fecha_inic = fecha_inic
        self.__fecha_fin = fecha_fin
    
    def getReserva(self):
        return "El ID de la reserva es: ",str(self.__id_reserva) +", el tipo de habitacion es: "+ str(self.__id_tipohab) +", La fecha de inicio es: "+ self.__fecha_inic +", La fecha final es: "+ self.__fecha_fin
        
    # def getHabitaciones(self):
    #     return str(self.__id_tipohab) +","+ str(self.__habi_disp)
        







# Funcion hecha para el registro de la reserva hecha de una habitacion
def RegistrarReserva():
    print("//Biervenido al sistema de registro de reserva, se requiere que siga los siguientes pasos//")
    
    nombre_usuario = input("Digite su nombre: ")
    apellido_usuario = input("Digite su apellidos: ")
    habitaciones = int(input("Digite cuantas habitaciones va a reservar: "))
    id_usuario = int(input("Digite su id de usuario: "))
    personas = int(input("Digite cuantas personas se hospedaran en la habitacion: "))
    print("1. Sencilla \n2. Doble \n3. Familiar \n4. Suite \n5. Presidencial")
    tipo_hab = int(input("Elija el tipo de habitacion en la cual se hospedara: "))
    fecha_inic = input("Digite el inicio de la fecha de su estadia (AAAA-MM-DD):")
    fecha_fin = input("Digite el fin de la fecha de su estadia (AAAA-MM-DD):")


    conexion =  sqlite3.connect("C:\\Users\\ta872\\OneDrive\\Escritorio\\Sena\\Program\\3 trimestre\\olympo\\olympo.db")
    cursor = conexion.cursor()
    sentenciaReserva = str(f"INSERT INTO tb_Reserva (idusuario_usuarioRes, idtipo_habRes, personasRes, fechainicioRes, fechafinRes, canhabitacionesRes) VALUES('{id_usuario}', '{tipo_hab}', '{personas}', '{fecha_inic}','{fecha_fin}', '{habitaciones}')")
    sentencia_id_reserva = str(f"SELECT id_reservaRes FROM tb_Reserva where idusuario_usuarioRes = ('{id_usuario}')")
    cursor.execute(sentenciaReserva)
    id_reserva = cursor.execute(sentencia_id_reserva)
    lista=id_reserva.fetchall()
    print(lista[0])
    Res = Reserva(lista, tipo_hab, habitaciones, fecha_inic, fecha_fin)
    Usu = Usuario(nombre_usuario, apellido_usuario, id_usuario)
    print(Res.getReserva())
    print(Usu.getUsuario())
    conexion.commit()
    conexion.close()
    
    # print(Res.getHabitaciones())


#Eliminacion de Reserva
def eliminacionReserva():
    conexion = sqlite3.connect("C:\\Users\\ta872\\OneDrive\\Escritorio\\Sena\\Program\\3 trimestre\\olympo\\olympo.db")
    cursor = conexion.cursor()
    print("//Bienvenido al sistema de eliminacion de reservas//")
    id_eliminacion = int(input("Digite el ID de la reserva que se va a cancelar: "))
    sentencia_eliminacion = str(f"DELETE FROM tb_Reserva where id_reservaRes = ('{id_eliminacion}')")
    cursor.execute(sentencia_eliminacion)
    print("Eliminacion Exitosa")
    conexion.commit()
    conexion.close()
    


def actualizacionReserva():
    conexion = sqlite3.connect("C:\\Users\\ta872\\OneDrive\\Escritorio\\Sena\\Program\\3 trimestre\\olympo\\olympo.db")
    cursor = conexion.cursor()
    print("//Bienvenido al sistema de actualizacion de reservas//")

    id_reservact = int(input("Para seguir con el proceso digite el ID de la reserva: "))

    print("1. Tipo de habitacion \n2. Cantidad de Habitaciones a reservar \n3. Personas que se hospedaran \n4. Fecha de inicio de reserva \n5. Fecha final de reserva")
    actu = int(input("Digite el proceso que quiere que se cambie: "))

    if actu == 1:
        print("1. Sencilla \n2. Doble \n3. Familiar \n4. Suite \n5. Presidencial")
        id_tipoactu = int(input("Digite el tipo de habitacion: "))
        sentenciatipo = str(f"UPDATE tb_Reserva SET idtipo_habRes = ('{id_tipoactu}') WHERE id_reservaRes = ('{id_reservact}') ")
        cursor.execute(sentenciatipo)
        print("Actualizacion Completada")
        conexion.commit()
        conexion.close()
    elif actu == 2:
        cantidadhabi = int(input("Digite el numero de habitaciones a reservar: "))
        sentenciacant = str(f"UPDATE tb_Reserva SET canhabitacionesRes = ('{cantidadhabi}') WHERE id_reservaRes = ('{id_reservact}')")
        cursor.execute(sentenciacant)
        print("Actualizacion Completada")
        conexion.commit()
        conexion.close()
    elif actu == 3:
        cantidadper = int(input("Digite el numero de personas: "))
        sentenciaper = str(f"UPDATE tb_Reserva SET personasRes = ('{cantidadper}') WHERE id_reservaRes = ('{id_reservact}')")
        cursor.execute(sentenciaper)
        print("Actualizacion Completada")
        conexion.commit()
        conexion.close()
    elif actu == 4:
        FechaIniac = input("Digite la nueva fecha de inicio de la reserva: ")
        sentenciainic = str(f"UPDATE tb_Reserva SET fechainicioRes = ('{FechaIniac}') WHERE id_reservaRes = ('{id_reservact}')")
        cursor.execute(sentenciainic)
        print("Actualizacion Completada")
        conexion.commit()
        conexion.close()
    elif actu == 5:
        FechaFinac = input("Digite la nueva fecha de inicio de la reserva: ")
        sentenciaFin = str(f"UPDATE tb_Reserva SET fechafinRes = ('{FechaFinac}') WHERE id_reservaRes = ('{id_reservact}')")
        cursor.execute(sentenciaFin)
        print("Actualizacion Completada")
        conexion.commit()
        conexion.close()
        




def menures():
    print("//Bienvenido al sistema de Registro de Reserva//")
    print("")
    print("El sistema posee los siguientes servicios \n1. Registrar Reserva \n2. Eliminar Reserva \n3. Actualizar Reserva")
    Resposta = int(input("Digite la opcion a seguir: "))
    if Resposta == 1:
        RegistrarReserva()
    elif Resposta == 2:
        eliminacionReserva()
    elif Resposta == 3:
        actualizacionReserva()
   