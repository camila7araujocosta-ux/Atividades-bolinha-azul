#Algoritmo que receba um número
n = float(input("Digite um número: "))

#Se for par e positivo; Se for par e negativo; Caso contrário → “Ímpar”
if (n % 2 == 0 and n > 0):
    print("O número é par e positivo")
elif (n % 2 == 0 and n < 0): 
    print("O número é par e negativo")
else:
    print("O número é ímpar")        
print("Fim do programa")       