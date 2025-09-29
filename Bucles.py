#Existen 2 tipos de bucles
#while & for

#Algo que puedo decir de esos 2 es que se diferencian
#while se repite infinitamente hasta que algo rompa el bucle
#for se repite una finita de veces determinada

#while
#especificamente 'while True:'
#esta es su estructura

#while True:
#  (Aqui pones lo que quieres que se repita)
#  continue (sirve para que el bucle siga)
#  break (sirve para romper el bucle while)

#Ejemplo de while:
while True:
  v = input()
  if v == "": #si la variable v es igual a una cadena de texto vacia...
    break #se rompe el bucle
  else: #caso contrario...
    continue #el bucle continua

#de while tambien existe su version False
#pero solo trabajaremos con 'while True:'
#dado a que 'while False:' no se ejecuta nunca
#asi que continuemos con...

#for
#a comparacion de while no se repite infinitamente hasta que algo rompa el bucle
#for se repite una cantidad de veces determinada
#su estructura es la siguiente
#for variable in range(parametro):
#  (Aqui pones lo que quieres que se repita)

#Ejemplo de for:
for i in range(5): #la variable i tomara valores del 0 al 4 (si especificamente numeros enteros)
  print(i) #imprime el valor de i osea 0, 1, 2, 3, 4 (siempre se empieza desde 0)
#si quieres que empieze desde otro numero diferente a 0

#Explicare lo que tiene el ejemlo de for
#for por si solo es una palabra clave que indica que se va a iniciar un bucle for
#la variable i es una variable cualquiera que tomara los valores del rango que le digamos
#in simplemente busca dentro de algo que en este caso lo buscaria en el rango 'range(5)'
#range() establece un rango tal cual el numero lo podemos cambiar para que se repita las veces que queramos
