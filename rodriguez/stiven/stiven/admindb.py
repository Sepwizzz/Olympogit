import sqlite3
#contenido=sqlite3.connect("C:C:\proyecto\Olympogit\db olympo/olympo.db")
#---------------------------------------------------------
ruta="C:\olympobase"
#---------------------------------------------------------
class admin:
    def __init__(self) :
        print("hola")
        

    def agregarh():
        
        numerod_h=int(input("ponga el numero de habitacion :"))
        descrpcion=input("ponga una descripcion :")
        inventario=int(input("ponga numero de inventario :"))


        contenido=sqlite3.connect(ruta+"/olympo.db")
        cursor=contenido.cursor()
        agregar=str(f"INSERT INTO tb_Habitacion VALUES ({numerod_h},'{descrpcion}',{inventario})")
        cursor.execute(agregar)
        contenido.commit()
        contenido.close()
    
    def eliminarh():
    
        numerod_h=int(input("ponga el numero de habitacion a eliminar :"))
        


        contenido=sqlite3.connect(ruta+"/olympo.db")
        cursor=contenido.cursor()
        eliminar=str(f"DELETE FROM tb_Habitacion WHERE id_habitacionHab = {numerod_h}")
        cursor.execute(eliminar)
        contenido.commit()
        contenido.close()

    def actualizarh():
        print("---------\nque quiere actualizar\n---------\nnueva descercion = 1\nnuevo Moviliario = 2\n---------")
        decicion=input("que opcion escogio :")
        match decicion:

            case "1":
                print("------------------------------------------------\nusted esta actualizando la descripcion\n------------------------------------------------")
                numerod_h=int(input("ponga el numero de habitacion a actulizar :"))
                newd=input("ponga nueva descripcion :")
                contenido=sqlite3.connect(ruta+"/olympo.db")
                cursor=contenido.cursor()
                actualizar=str(f"UPDATE tb_Habitacion SET descripcionHab = '{newd}' WHERE id_habitacionHab = {numerod_h}")
                cursor.execute(actualizar)
                contenido.commit()
                contenido.close()
            case "2":
                print("------------------------------------------------\nusted esta actualizando el moviliario\n------------------------------------------------")
                numerod_h=int(input("ponga el numero de habitacion a actulizar :"))
                newm=int(input("ponga el numero de moviliario  :"))
                contenido=sqlite3.connect(ruta+"/olympo.db")
                cursor=contenido.cursor()
                actualizar=str(f"UPDATE tb_Habitacion SET idmobiliarioHab = {newm} WHERE id_habitacionHab = {numerod_h}")
                cursor.execute(actualizar)
                contenido.commit()
                contenido.close()
    def visualizarh():
        print("todo =1 una habitacion=2")
        deci=input("que decide :")
        match deci:
            case "1":
                contenido=sqlite3.connect(ruta+"/olympo.db")
                cursor=contenido.cursor()
                agregar=str(f"select * from tb_Habitacion ")
                cursor.execute(agregar)
                lista=cursor.fetchall()
                contenido.commit()
                contenido.close() 
                print(format(lista))       
            case "2":
                numerod_h=int(input("ponga el numero de habitacion :"))
                contenido=sqlite3.connect(ruta+"/olympo.db")
                cursor=contenido.cursor()
                agregar=str(f"select * from tb_Habitacion WHERE id_habitacionHab = {numerod_h}")
                cursor.execute(agregar)
                lista=cursor.fetchall()
                contenido.commit()
                contenido.close() 
                print(lista)       
#--------------------------------------------------------------------------------------------------------------
    def agregarfun():
        
        cc=int(input("ponga el numero de CEDULA :"))
        nombre=input("ponga Nombre del travajador :")
        contacto=input("ponga el contacto del travajador :")
        cargo=int(input("ponga el cargo del trabajador :"))
        estrato=int(input("ponga el estrato del trbajdor :"))
        salario=input("ponga el salario del trabjador :")
        eps=input("ponga la eps del trabjador :")
        arl=input("ponga la arl :")
        cajacompe=input("ponga la caja de compesasion :")
        fechaini=input("ponga la fecha de inicio del contrato  :")
        fechafin=input("ponga la fecha de fin del contrato :")
        



        contenido=sqlite3.connect(ruta +"/olympo.db")
        cursor=contenido.cursor()
        agregarfun=str(f"INSERT INTO tb_Funcionarios (idusuarioFun,nombreFun,contactoFun,idtipousuFun,estratoFun,salarioFun,epsFun,ArlFun,cajacompFun,fechainicioFun,fechafinFun) VALUES ({cc},'{nombre}','{contacto}',{cargo},{estrato},'{salario}','{eps}','{arl}','{cajacompe}','{fechaini}','{fechafin}')")
        cursor.execute(agregarfun)
        contenido.commit()
        contenido.close()   
    
    def eliminarfun():
    
        numero_cc=int(input("ponga el numero de cedula del travajador :"))
        


        contenido=sqlite3.connect(ruta+"/olympo.db")
        cursor=contenido.cursor()
        eliminar=str(f"DELETE FROM tb_Funcionarios WHERE idusuarioFun = {numero_cc}")
        cursor.execute(eliminar)
        contenido.commit()
        contenido.close()
    def actualizarfun():
        print("---------\nque quiere actualizar\n---------\nnueva contacto = 1\nnuevo cargo = 2\nnueva eps = 3\nnuevo fecha fin = 4\n---------")
        decicion=input("que opcion escogio :")
        match decicion:

            case "1":
                print("------------------------------------------------\nusted esta actualizando el contacto\n------------------------------------------------")
                cc_usu=int(input("ponga el numero de cedula del trabajador  :"))
                new_contacto=input("ponga nuevo contacto :")
                contenido=sqlite3.connect(ruta+"/olympo.db")
                cursor=contenido.cursor()
                actualizar=str(f"UPDATE tb_Funcionarios SET contactoFun = '{new_contacto}' WHERE idusuarioFun = {cc_usu}")
                cursor.execute(actualizar)
                contenido.commit()
                contenido.close()
            case "2":
                print("---------\nsolo cargo= 1\ncargo y salrio= 2\n---------")
                decicioncar=input("que quiere actualizar")
                match decicioncar:

                    case "1":
                        print("------------------------------------------------\nusted esta actualizando el cargo\n------------------------------------------------")
                        cc_usu=int(input("ponga el numero de cedula del trabajador  :"))
                        new_cargo=input("ponga nuevo cargo :")
                        contenido=sqlite3.connect(ruta+"/olympo.db")
                        cursor=contenido.cursor()
                        actualizar=str(f"UPDATE tb_Funcionarios SET idtipousuFun = {new_cargo} WHERE idusuarioFun = {cc_usu}")
                        cursor.execute(actualizar)
                        contenido.commit()
                        contenido.close() 
                    case "2" :
                        print("------------------------------------------------\nusted esta actualizando el cargo\n------------------------------------------------")
                        cc_usu=int(input("ponga el numero de cedula del trabajador  :"))
                        new_cargo=input("ponga nuevo cargo :")
                        new_salrio=input("ponga el nuevo salario")
                        contenido=sqlite3.connect(ruta+"/olympo.db")
                        cursor=contenido.cursor()
                        actualizar=str(f"UPDATE tb_Funcionarios SET idtipousuFun = {new_cargo} , salarioFun = '{new_salrio}' WHERE idusuarioFun = {cc_usu}")
                        cursor.execute(actualizar)
                        contenido.commit()
                        contenido.close() 
            case "3":
                print("------------------------------------------------\nusted esta actualizando el eps\n------------------------------------------------")
                cc_usu=int(input("ponga el numero de cedula del trabajador  :"))
                new_eps=input("ponga nueva eps :")
                contenido=sqlite3.connect(ruta+"/olympo.db")
                cursor=contenido.cursor()
                actualizar=str(f"UPDATE tb_Funcionarios SET epsFun = '{new_eps}' WHERE el salario = {cc_usu}")
                cursor.execute(actualizar)
                contenido.commit()
                contenido.close() 
            case "4":
                print("------------------------------------------------\nusted esta actualizando el fecha fin\n------------------------------------------------")
                cc_usu=int(input("ponga el numero de cedula del trabajador  :"))
                new_fechafin=input("ponga la nueva fecha fin :")
                contenido=sqlite3.connect(ruta+"/olympo.db")
                cursor=contenido.cursor()
                actualizar=str(f"UPDATE tb_Funcionarios SET fechafinFun = '{new_fechafin}' WHERE idusuarioFun = {cc_usu}")
                cursor.execute(actualizar)
                contenido.commit()
                contenido.close()  
    def visualizarfun():
        print("todo =1 un trbajador=2")
        deci=input("que decide :")
        match deci:
            case "1":
                contenido=sqlite3.connect(ruta+"/olympo.db")
                cursor=contenido.cursor()
                agregar=str(f"select * from tb_Funcionarios ")
                cursor.execute(agregar)
                lista=cursor.fetchall()
                contenido.commit()
                contenido.close() 
                print("-"*20)
                for o in lista:
                    
                    print(o[0])
                    print(o[1])
                    print(o[2])
                    print(o[3])
                    print(o[4])
                    print(o[5])
                    print(o[6])
                    print(o[7])
                    print(o[8])
                    print(o[9])
                    print(o[10])
                    print("-"*20)
            case "2":
                cc_usu=int(input("ponga el numero de habitacion :"))
                contenido=sqlite3.connect(ruta+"/olympo.db")
                cursor=contenido.cursor()
                agregar=str(f"select * from tb_Habitacion WHERE WHERE idusuarioFun = {cc_usu}")
                cursor.execute(agregar)
                lista=cursor.fetchall()
                contenido.commit()
                contenido.close() 
                print(lista)          
#-----------------------------------------------------------------                
    def agregarservi():
        
        descripcion=input("ponga el nombre del servicio :")
        valor=int(input("ponga el valor del servicio :"))
        


        contenido=sqlite3.connect(ruta+"/olympo.db")
        cursor=contenido.cursor()
        agregaservi=str(f"INSERT INTO tb_Sservicios (descripcionS,valorS) VALUES ('{descripcion}',{valor})")
        cursor.execute(agregaservi)
        contenido.commit()
        contenido.close()  

    def eliminarservi():
    
        nemroservi=int(input("ponga el numero del servicio :"))
        


        contenido=sqlite3.connect(ruta+"/olympo.db")
        cursor=contenido.cursor()
        eliminar=str(f"DELETE FROM tb_Sservicios WHERE idServicio = {nemroservi}")
        cursor.execute(eliminar)
        contenido.commit()
        contenido.close()
    def actualizarservi():
        print("---------\nque quiere actualizar\n---------\nnueva descripcion = 1\nnuevo valor = 2\n---------")
        decicion=input("que opcion escogio :")
        match decicion:

            case "1":
                print("------------------------------------------------\nusted esta actualizando la descripcion\n------------------------------------------------")
                numerod_servi=int(input("ponga el numero del servicio a actulizar :"))
                newdesS=input("ponga nueva descripcion :")
                contenido=sqlite3.connect(ruta+"/olympo.db")
                cursor=contenido.cursor()
                actualizar=str(f"UPDATE tb_Sservicios SET descripcionS = '{newdesS}' WHERE idServicio = {numerod_servi}")
                cursor.execute(actualizar)
                contenido.commit()
                contenido.close()
            case "2":
                print("------------------------------------------------\nusted esta actualizando el moviliario\n------------------------------------------------")
                numerod_servi=int(input("ponga el numero del servicio a actulizar :"))
                newm=int(input("ponga el nuevo precio  :"))
                contenido=sqlite3.connect(ruta+"/olympo.db")
                cursor=contenido.cursor()
                actualizar=str(f"UPDATE tb_Sservicios SET valorS = {newm} WHERE idServicio = {numerod_servi}")
                cursor.execute(actualizar)
                contenido.commit()
                contenido.close()
    def visualizarservi():
        print("todo =1 una trbajador=2")
        deci=input("que decide :")
        match deci:
            case "1":
                contenido=sqlite3.connect(ruta+"/olympo.db")
                cursor=contenido.cursor()
                agregar=str(f"select * from tb_Sservicios ")
                cursor.execute(agregar)
                lista=cursor.fetchall()
                contenido.commit()
                contenido.close() 
                print("-"*20)
                for o in lista:
                    print(o[0])
                    print(o[1])
                    print(o[2])
                    print("-"*20)
            case "2":
                numerod_servi=int(input("ponga el numero de servicio :"))
                contenido=sqlite3.connect(ruta+"/olympo.db")
                cursor=contenido.cursor()
                agregar=str(f"select * from tb_Sservicios  WHERE idServicio = {numerod_servi}")
                cursor.execute(agregar)
                lista=cursor.fetchall()
                contenido.commit()
                contenido.close() 
                print(lista)      

                    
          
        
         
  



#a=admin
#a.eliminarh()
#a.agregarh()
#a.actualizarh()
#a.visualizarh()
#------------
#a.agregarfun()
#a.eliminarfun()
#a.actualizarfun()
#a.visualizarfun()
#---------------
#a.agregarservi()
#a.eliminarservi()
#a.actualizarservi()
#a.visualizarservi()
