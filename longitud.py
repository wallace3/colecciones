palabra = input("Ingresa una palabra")

if len(palabra) < 4:
   print("Hacen falta letras, solo tiene", len(palabra), "letras") 
elif len(palabra) > 8:
   print("Sobran letras, tiene ", len(palabra), "letras ")
else:
   print("Palabra correcta")