## PROGRAMA LONGITUD DE PALABRA ##

palabra = input("Ingresa una palabra")    #Se solicita una palabra al usuario 

if len(palabra) < 4:
   print("Hacen falta letras, solo tiene", len(palabra), "letras")      #Si la palabra tiene menos de 4 letras, se muestra el mensaje con las que tiene
elif len(palabra) > 8:
   print("Sobran letras, tiene ", len(palabra), "letras ")   #Si la palabra tiene más de 8 letras, es muestra las letras sobrantes
else:
   print("Palabra correcta")   #Si se cumple la condición, es palabra correcta

## FIN DEL PROGRAMA  ##




## PROGRAMA PARA UBICAR EN CUADRANTE ##

coordenadas = {"cuadrante1":(True,True), "cuadrante2":(False,True), "cuadrante3":(False,False), "cuadrante4":(True,False)} #Se declara la lista con tupla de los posibles cuadrantes

#Se comienza a solicitar al usuario los números.
x = int(input("Ingresa coordenada X"))
y = int(input("Ingresa coordenada Y"))

if x == 0 or y == 0:
    print('Ninguna coordenada solicitada debe ser igual a 0')    #Se evalua que el ninguno de los números ingresados sea igual a 0
else:                       
    geolocalizacion = (x>0,y>0)     #Se aplica una condición para evaluar si es True o False para comparar con la lista anterior.
    for coordenada in coordenadas:  # Se crea un ciclo para recorrer la lista y compararla con las coordenadas ingresadas por el usuario.
        if geolocalizacion == coordenadas[coordenada]:
            print("Se encuentra en el ", coordenada)     #En caso que se encuentra una concidencia, se muestra el resultado del cuadrante donde se encuentra y termina el ciclo
            break
        else:
            continue   #Si no se encuentra coincidencia la vuelta del ciclo actual, continua con el ciclo

## FIN DEL PROGRAMA ##




