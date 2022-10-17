limite_mayor = int(input("Dime el limite mayor "))
limite_menor = int(input("Dime el limite menor "))

while limite_menor > limite_mayor:
    limite_menor = int(input(f"El limite menor no puede ser superior a {limite_mayor}. Dime el limite menor "))

numero = int(input(f"Introduzca un número entero {limite_menor} y {limite_mayor}"))

suma = 0
fuera = 0
igual = 0

while numero!=0:
    
    
    if limite_menor < numero < limite_mayor:
        suma+=numero
    elif numero < limite_menor or numero > limite_mayor:
        fuera+=1
    else:
        igual+=1
    numero = int(input(f"Introduzca un numero entre {limite_menor} y { limite_mayor}: "))

print(f"La suma de los numeros dentro del intervalo es {suma}, fuera del intervalo hay {fuera} numeros")
print(f"Exite {igual} numeros que coinciden con los limites del intervalo")

print("------------------")

pago = 10
suma= pago

for i in range(2,21):
    pago*=2
    print(f"El pago del mes {i} es {pago}")
    suma+=pago
print(f"Ha salido baratito, son son {suma}€")

numero=0
total=(2**20)*10
print(f"La suma es {total} ")