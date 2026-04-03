#Algoritmo que leia idade
a = int(input("Digite um número: "))

#Mostre: Menor de idade (<18); Adulto (18 a 59); Idoso (60+).
if (a < 18): 
    print("Menor de idade")
elif (a >= 18 and a <= 59):
    print("Adulto") 
elif (a >= 60):
    print("Idoso")
print("Fim do algoritmo")        