from admindb import*

a=admin      
print("------------------------------\nhabitacion=1\nfuncionario=2\nservicio=3\n------------------------------")
decicion1=input("ponga decicion :")
print("------------------------------")

match decicion1:
    case "1":
        print("------------------------------\nagregar habitacion=1\neliminar habitcion=2\nactualizar habitacion=3\nvisualizar habitacion=4\n------------------------------")
        decicionh=input("que decide :")
        print("------------------------------")
        match decicionh:

            case "1":
                a.agregarh()
            case "2":
                a.eliminarh()
            case "3":
                a.actualizarh()
            case "4":
                a.visualizarh()

    case "2":
        print("------------------------------\nagregar funcioario=1\neliminar funcioario=2\nactualizar funcioario=3\nvisualizar funcioario=4\n------------------------------")
        decicionfun=input("que decide :")
        print("------------------------------")
        match decicionfun:

            case "1":
                a.agregarfun()
            case "2":
                a.eliminarfun()
            case "3":
                a.actualizarfun()
            case "4":
                a.visualizarfun()
    case "3":
        print("------------------------------\nagregar servicio=1\neliminar servicio=2\nactualizar servicio=3\nvisualizar servicio=4\n------------------------------")
        decicionfun=input("que decide :")
        print("------------------------------")

        match decicionfun:

            case "1":
                a.agregarservi()
            case "2":
                a.eliminarservi()
            case "3":
                a.actualizarservi()
            case "4":
                a.visualizarservi()
                