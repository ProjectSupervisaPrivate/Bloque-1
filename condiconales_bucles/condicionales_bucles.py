#Ejemplo 9
#Este ejemplo nos devuelve los numeros que son divisibles entre 2 de forma exacta
encontrado = False
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9
,10, 11, 12, 13, 14] #Creamos la lista con números
for num in numeros: #En la variable "num" almacenamos los ítem de la lista
    if num % 4 == 0: #Condición: Si el resto de la división por
        print (num) # Imprimimos la variable num
        encontrado = True
    if encontrado == False:
        print("Seguimos")
        
