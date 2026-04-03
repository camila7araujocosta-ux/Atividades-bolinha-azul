#Algoritmo que Leia um número
n = float(input("Digite um número: "))

#Se for maior que 100 → mostre metade; Senão → mostre o dobro.
if (n > 100):
    print("A metade do número é: ", n / 2)
else:
    print("O dobro do número é: ", n * 2)
print("Fim do programa")