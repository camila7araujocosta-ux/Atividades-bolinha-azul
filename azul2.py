#Algoritmo que leia dois números
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

#Mostre a soma
S = n1 + n2
print("O resultado da soma é: ", S)

#Mostre qual é maior ou se são iguais
if (n1 > n2): 
    print("O número", n1, "é maior que", n2)
elif (n2 > n1): 
    print("O número", n2, "é maior que", n1)
else: 
    print("Os números são iguais")
print("Fim do programa")           