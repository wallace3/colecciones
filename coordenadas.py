coordenadas = {"cuadrante1":(True,True), "cuadrante2":(False,True), "cuadrante3":(False,False), "cuadrante4":(True,False)}

x = int(input("Ingresa coordenada X"))
y = int(input("Ingresa coordenada Y"))

if x == 0 or y == 0:
    print('Ninguna coordenada solicitada debe ser igual a 0')
else:
    geolocalizacion = (x>0,y>0)
    for coordenada in coordenadas:
        if geolocalizacion == coordenadas[coordenada]:
            print("Se encuentra en el ", coordenada)
            break
        else:
            continue




