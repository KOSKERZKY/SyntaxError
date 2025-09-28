
#Unicamente usaremos:
#Todos los aritmeticos
#Todos los comparativos
#Puede que de logica
#Lo demas por el momento NO

#Lo que dejare en la parte inferior son avanzados ya a un nivel mas nerd 

# 1. Aritméticas
a = 10
b = 3
print(a + b)   # suma → 13
print(a - b)   # resta → 7
print(a * b)   # multiplicación → 30
print(a / b)   # división → 3.333...
print(a // b)  # división entera → 3
print(a % b)   # módulo/resto → 1
print(a ** b)  # potencia → 1000

# 2. Comparación
print(a == b)  # igual a → False
print(a != b)  # diferente de → True
print(a > b)   # mayor que → True
print(a < b)   # menor que → False
print(a >= b)  # mayor o igual → True
print(a <= b)  # menor o igual → False

# 3. Lógicas
x = True
y = False
print(x and y)  # y → False
print(x or y)   # o → True
print(not x)    # no → False

# 4. Asignación
c = 5
c += 2  # equivalente a c = c + 2 → 7
c -= 1  # c = c - 1 → 6
c *= 3  # c = c * 3 → 18
c /= 2  # c = c / 2 → 9.0
c //= 4 # c = c // 4 → 2.0
c %= 2  # c = c % 2 → 0.0
c **= 3 # c = c ** 3 → 0.0

# 5. Pertenencia
lista = [1, 2, 3]
print(2 in lista)      # True
print(5 not in lista)  # True

# 6. Identidad
d = [1,2]
e = d
f = [1,2]
print(d is e)     # True, mismo objeto
print(d is f)     # False, mismo contenido pero distinto objeto
print(d is not f) # True

# 7. Bit a bit (esto tiene que ver con la representacion binaria)
p = 6   # 110
q = 3   # 011
print(p & q)   # AND → 2
print(p | q)   # OR → 7
print(p ^ q)   # XOR → 5
print(~p)      # NOT → -7
print(p << 1)  # desplazamiento izquierda → 12
print(p >> 1)  # desplazamiento derecha → 3
