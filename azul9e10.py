#Algoritmo que leia dois números
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

#Verifique se são iguais ou diferentes. Sendo diferentes mostre a diferença entre eles
if (n1 == n2):
    print("Os números são iguais")
else:
    print("Os números são diferentes")
    print("A diferença entre eles é:", abs(n1 - n2))
print("Fim do programa")    



#Algoritmo que leia um número
a = float(input("Digite um número: "))

#verifique se eles estão entre 0 e 100, caso o número esteja fora do intervalo, mostre na tela o valor.
if (a >= 0 and a <= 100):
    print("O número está entre 0 e 100")
else:
    print("O número está fora do intervalo, o valor é: ", a)
print("Fim do programa")        