#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Em seguida, calcule a média anual das temperatura e mostre a média calculada juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 
#1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ["Janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outrubro","novembro","dezembro"]
temperaturas = []
temp_acima = []

for i in range(12):
    temp = float(input(f"digite a temperatura do mês de {meses [i]}:  "))
    temperaturas.append(temp)

media_anual = sum(temperaturas) / len(temperaturas)
print("a média anual das temperaturas é: ",media_anual)
for it in temperaturas:
    if it > media_anual:
        temp_acima.append(it)
    
print("as temperaturas acima são:")

for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{meses[i]}: {temperaturas[i]}°C")