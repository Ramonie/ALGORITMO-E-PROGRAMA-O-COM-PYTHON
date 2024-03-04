from shutil import which


print(" Escreva um algoritmo para ler o número de votos brancos, nulos e válidos.")
print("Calcular e escrever o percentual que cada um representa em relação ao total de eleitores")

print("--------------MENU-------------")
print("---[1] - Prefeito Raimundo---")
print("---[2] - Prefeito Francisco---")   
print("---[S] - Sair------------------")   
cont= 0
contf=0
contr=0
c = 0
i = 0
r = 0
str(input('Escolha uma opção: '))

if (c):
        print("Voto armazenado")
        cont= cont+1
elif(r):
        print("Votado")
        contr=contr+1
else:
        print("Obrigado por votar")

