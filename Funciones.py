#Aqui aprenderas a definir una funcion
#Puedes llamar una o mas palabras clave sin tener que escribirlas de nuevo solo llamando a la variable donde se encuentran
#La palabra clave para crear una variable es definir una funcion es usar 'def'
#Estructura: 
def nombre_funcion(parametro): #los parametros son opcionales
  """cuerpo 
  de 
  la 
  funcion"""
  return

#Pondre un ejemplo
def suma(a, b): #definimos una funcion y los parametros que se deben rellenar 
  return a + b #el resultado esta guardado en esta funcion cuando se llama  un dato es que return solo se puede usar en funciones

s = suma(5 + 3) #Aqui llamamos a la funcion 'suma()' y le asignamos valores para a y b
print(s) # 8 

#Existe una manera de hacer que ahorrarce el poner print() cada que quieres mostrar el resultado y es poniendolo dentro de la funcion
def resta(a, b): #definimos una funcion y los parametros que se deben rellenar
  print(a - b) #imprime automaticamente cuando se llama la funcion

resta(5, 3) #2

#es de a conforme tus preferencias si quieres usar la funcion con 'return' o con 'print()'
