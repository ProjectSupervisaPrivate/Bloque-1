#Ejemplo 7
#Las listas son conjuntos ordenados de elementos (numeros, cadenas, etc). Las listas se delimitan por corchetes ([ ]) y los elementos se separan por comas.
#crear una lista
thislist = ["apple", "banana", "cherry"]
print(thislist)

#tambien se pueden crear listas combinando diferentes tipos de datos
thislist = [1, 10.0, "cherry"]
print(thislist)

#imprimir el segundo elemento de una lista
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#imprimir el ultimo elemento de una lista
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#imprimir el tercero, cuarto y quinto elemento de una lista
thislist = [1, 2, 3, 4, 5, 6, 7]
print(thislist[2:5])

#Accediendo un indice que no exista generara un error.
mylist = [1,2,3]
print (mylist[10])

#cambiar el valor del segundo elemento de una lista
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#append nos permite añadir valores consecutivos a nuestra lista
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#mediante insert podemos añadir un elemento una lista en una posicion concreta
thislist.insert(2, 'a')
print(thislist)

#eliminar un elemento de la lista
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#eliminar un elemento de la lista mediante el indice
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#limpiar una lista
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#unir dos listas
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#el metodo index() busca el indice de un elemento en la lista
my_list = ['a','b','c']
index = my_list.index('b')
print(index)

#imprimir el tamanio de una lista
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#contar cuanto se repite un determinado elemento de una lista
fruits = ['cherry', 'apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

#ordenar una lista
#ordenar decreciente

x = [4, 6, 3, -5]
x.sort()
print(x)

#ordenar creciente

x = [4, 6, 3, -5]
x.sort(reverse = True)
print(x)

