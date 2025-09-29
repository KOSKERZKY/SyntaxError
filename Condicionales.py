#Aqui utilizaremos palabras claves como 'if', 'elif' y 'else'
#if (expresa que hara algo si ocurre lo que nosotros le dijimos que tenia que pasar)
#elif (hace otra cosa si 'if' no fue correcto a lo que le dijimos)
#else (hace algo si ninguna de las anteriores es correcta)

#Me explico muy confunso pero con un ejemplo espero lo puedas entender
edad = int(input("Cual es tu edad? ")) #input() suelta la cifra que ingresemos como cadena de texto pero esta encerrado por int() quiere decir que todo lo ingresado hay se hara un numero entero
if edad >= 18: #si la variable edad tiene un numero mayor o igual a 18 se mostrara 'Eres mayor de edad'
  print("Eres mayor de edad")
else: #caso contrario mostrara 'Eres menor de edad'
  print("Eres menor de edad")
#Este ejemplo es de un libro de robotica

#Aprovecho a explicar otro ejemplo de condicionales de ese libro
precio = float(input("Ingresa el precio del producto: ")) #transforma la cifra en un decimal por ejemplo 1 -> 1.00
if precio >= 100: #Si la variable 'precio' tiene un valor mayor a 100...
  descuento = precio * 0.1 #Se crea una variable que contiene el valor de 'precio' multiplicado por 0.1 que vendria siendo 
  precio_con_descuento = precio - descuento #Se crea una variable que resta el valor de 'precio' con la variable 'descuento'
  print("Se aplica un 10% de descuento") #Imprime esto en la ventana
  print("Precion con descuento: ", precio_con_descuento) #Imprime el texto y el valor de 'precio_con_descuento'
else: #Caso contrario...
  print("No hay descuento") #Imprime esto en la ventana
