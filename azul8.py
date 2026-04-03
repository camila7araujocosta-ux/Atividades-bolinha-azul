#Algoritmo que leia um número
n = float(input("Digite um número: "))

#Mostre se ele é par positivo, par negativo, ímpar positivo, ímpar negativo ou neutro.
if (n % 2 == 0 and n >= 0):
    print("O número é par positivo")
elif (n % 2 == 0 and n < 0):
    print("O número é par negativo")
elif (n % 2 != 0 and n > 0): 
    print("O número é ímpar positivo")
elif (n % 2 != 0 and n < 0):
    print("O númeo é ímpar negativo")  
else: 
    print("O número é neutro")
print("Fim do programa")         