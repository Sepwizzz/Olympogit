
from rq1reserva import menures
from menuad import menucosasadmin

def menufin():
    print("hola bienvenido al menu\nreserva = 1\nmenu de admin =2")
    decicicon= int(input("ponga a que parte quiere ir :"))
    if decicicon==1:
        menures()
    elif decicicon ==2:
        menucosasadmin()
    elif decicicon ==0:
        print("gracias :)")
    elif decicicon==3:
        print("muy bien :")
         
    else:       
        print("-     -\npor favor haga lo que indica el menu\n-      -")
        
    

menufin()
