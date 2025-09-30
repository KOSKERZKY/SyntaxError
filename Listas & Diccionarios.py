#Las listas y diccionarios son estructuras de datos que permiten almacenar multiples valores en una sola variable
#Las listas son colecciones ordenadas de elementos, que pueden ser de diferentes tipos (int, float, str, bool, etc...)
#Los diccionarios son colecciones desordenadas de pares clave-valor

#Empezare diciendo que existen tipos de listas
#Listas #simples cumplen su funcion que es almacenar variedad de tipos de datos en una variable
#Listas anidadas #que son listas dentro de listas realmente se las puede agrupar cuantas veces se quieras se les llama listas nidificadas (nested list)
#Listas inmutables #el valor dentro de ellas no se puede cambiar y a esas se les llama tuplas (tuple)

#Estructura de una lista
#mi_lista = [elemento0, elemento1, elemento2, ...] #como aclare la indexacion siempre empieza en 0

#Estructura de una tupla
#mi_tupla = (elemento0, elemento1, elemento2, ...) #tambien se sigue cumpliendo de que la indexacion empieza en 0

#Estructura de un diccionario
#mi_diccionario = {clave1: valor1, clave2: valor2, clave3: valor3, ...} #las claves pueden ser de cualquier tipo de dato inmutable (str, int, float, bool, tuple) y los valores pueden ser de cualquier tipo de dato


#Mostrare ejemplos de cada una y una breve explicacion
#1. Listas simples
mi_lista = [1, 2.5, "txt", True] #una lista puede contener diferentes tipos de datos y aclarar nuevamente de que la indexacion siempre empieza en 0
print(mi_lista) #muestra toda la lista
print(mi_lista[2]) #muestra el tercer elemento de la lista

#Modificar elementos dentro de una lista
mi_lista[1] = 3.5 #cambia el valor del segundo elemento de la lista #el 2.5 ahora es 3.5
print(mi_lista) #muestra toda la lista actualizada
mi_lista.append("Nuevo elemento") #agrega un nuevo elemento #siempre se agrega al final de la lista
print(mi_lista) #muestra toda la lista actualizada
mi_lista.remove(2.5) #elimina el elemento 2.5 de la lista #.remove() es un metodo de lista que elimina el primer valor de la lista que coincida con el valor especificado
print(mi_lista) #muestra toda la lista actualizada
print(len(mi_lista)) #muestra la cantidad de elementos en la lista


#Un ejemplo de una lista anidada
#2. Listas anidadas (nested list)
mi_lista_anidada = [1, 2, [3, 4], ["Hola", "Mundo"]] #Las listas dentro de una lista se llaman sublistas cuentan como elementos de la lista principal
print(mi_lista_anidada) #muestra toda la lista anidada # 1, 2, [3, 4], ["Hola", "Mundo"]
print(mi_lista_anidada[2]) #muestra la tercera sublista # [3, 4]
print(mi_lista_anidada[2][1]) #muestra el segundo elemento de la tercera sublista # 4

#Modificar elementos dentro de una lista anidada
mi_lista_anidada[2].append(5) #agrega un nuevo elemento a la tercera sublista #con el valor de 5 # la lista ahora seria: [1, 2, [3, 4, 5], ["Hola", "Mundo"]]
print(mi_lista_anidada) #muestra toda la lista anidada actualizada # 1, 2, [3, 4, 5], ["Hola", "Mundo"]
mi_lista_anidada[3].remove("Hola") #elimina el elemento "Hola" de la cuarta sublista #aca remove() como metodo de lista elimina el valor 'Hola' dentro de la sublista [3]
print(mi_lista_anidada) #muestra toda la lista anidada actualizada


#Un ejemplo de una lista inmutable
#2. Listas inmutables (tuplas)
mi_tupla = (1, 2.5, "Hola", True) #una tupla puede contener diferentes tipos de datos
print(mi_tupla) #muestra toda la tupla # 1, 2.5, "Hola", True
print(mi_tupla[2]) #muestra el tercer elemento de la tupla # Hola
#a comparacion de las listas normales y anidadas aqui no puedes modificar los valores o eliminar valores dentro de la tupla



#las claves deben ser unicas dentro de un diccionario
#Los diccionarios no tienen un orden especifico como las listas
#Los diccionarios son utiles para almacenar datos relacionados entre si

#Un ejemplo de un diccionario
#3. Diccionarios
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30, 
    "ciudad": "Madrid"
} #un diccionario puede contener diferentes tipos de datos

print(mi_diccionario) #muestra todo el diccionario
print(mi_diccionario["nombre"]) #muestra el valor asociado a la clave "nombre" # Juan

#Modificar elementos dentro de un diccionario
mi_diccionario["edad"] = 31 #cambia el valor asociado a la clave "edad" #ahora la edad es 31
print(mi_diccionario) #muestra todo el diccionario actualizado
mi_diccionario["pais"] = "España" #agrega una nueva clave-valor al diccionario #clave "pais" con valor "España"
print(mi_diccionario) #muestra todo el diccionario actualizado
del mi_diccionario["ciudad"] #elimina la clave-valor asociada a la clave "ciudad"
print(mi_diccionario) #muestra todo el diccionario actualizado
print(len(mi_diccionario)) #muestra la cantidad de pares clave-valor en el diccionario


#si llegaste a entender todo tienes mi respeto :]
#se me complico mucho intentar explicarlo de una manera sencilla
#cualquier duda me puedes preguntar en mi ig: @jk3q0

#Manten realmente solo quiero que sepas la existencia de esos tipos de datos y para que sirve cada uno
# el uso de las listas depende de lo que quieras hacer :)
