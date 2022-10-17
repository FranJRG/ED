numero = int(input("Enter a number (negative to finish): "))

contador=0

while numero >= 0:
    contador+= 1
    numero = int(input("Enter a number (negative to finish: "))

print(f"You have entered {contador} positive numbers ")

print("------------------")



cantidad = int(input("How many numbers do you want input"))

while cantidad <= 0:
    cantidad = int(input("How many numbers do you want input"))

total, contador = 0,0

while cantidad>contador:
    numero = int(input("Enter one number greater than 0: "))
    while numero <=0:
        numero = int(input("The number is not valid, it should be greater than 0. Enter one number greater than 0: "))
    contador +=1
    total += numero

print(f"The medium is {total/cantidad} ")

print("-------------------")

numero = int(input("Enter an integer positive number"))
total = 1

if numero<0:
    print("The number is nota valid, try again")

else:
    for i in range(1, numero+1):
        total *=i
    
    print(total)
    
print("--------------------")

numero = int(input("Enter one number"))
pregunta =input("Do you want to enter more number (Y/N): ")
pequeño = numero

while pregunta.upper()=="Y":
    numero = int(input("Enter one number: "))
    if numero < pequeño:
        pequeño = numero
    pregunta = input("Do you want to enter more number (Y/N)? ")
    
print(f"The samallest nuumber is {pequeño}")

print("-------------------------")

cantidad = int(input("How many numbers do you want to input? "))

while cantidad <= 0:
    cantidad = int(input("The value is not right. How many numbers do you want input? "))


for i in range(cantidad):
    numero = int(input("Enter one number greater than 0: "))
    
    while numero <=0:
        numero = int(input("The number is not valid, it should be greater than 0: "))
    
    
    if numero%2==0:
        print(f"The number {numero} is even")
    else:
        print(f"The number {numero} is odd")   
        
print("-----------------------")

numero = int(input("Enter an integer positive number greater than 0: "))

while numero < 1:
    numero = int(input("The number is not valid, try again. "))

sumaD = 0
contandor=1

while numero > contador:
    if numero%contador == 0:
        sumaD+=contador
    contador+=1
'''
for i in range(1, (numero//2)+1):
    print(i)
    if numero%i==0:
        sumaD+=i
'''
if sumaD == numero:
    print("The number is perfect")
else:
    print("The number is not perfect")




       
    

   
   
   
   
   
   
   