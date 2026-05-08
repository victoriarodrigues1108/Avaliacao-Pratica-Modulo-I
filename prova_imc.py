#Nicolly Victoria
#Programa para calcular o de imc
print("=="*20)#replicação de caracteres
print("Programa para calcular o \"IMC\"".center(35))
print("=="*20)
print()
#informações do paciente
nome = input("Digite seu nome:")
idade = input("Digite sua idade:")
peso = float(input("Digite seu peso(KG):"))
altura = float(input("Digite sua altura altura(M):"))
print()
print("LAUDO MÉDICO")
#calcular o imc
imc = peso / (altura ** 2)
#Formatação do imc
print(f"{imc:.2f}")
#faixa de imc
if imc < 18.5:
    print("senhor(a)",nome,"seu IMC é:",imc,"portanto vocé está \"ABAIXO DO PESO\"")
elif imc < 24.9:
    print("senhor(a)",nome,"seu IMC é:",imc,"portanto vocé está com o \"PESO NORMAL\"")
elif imc < 29.9:
    print("senhor(a)",nome,"seu IMC é:",imc,"portanto vocé esta com o \"SOBREPESO\"")
elif imc < 34.9:
    print("senhor(a)",nome,"seu IMC é:",imc,"portanto vocé esta com \"OBESIDADE GRAU I\"")
elif imc < 39.9:
    print("senhor(a)",nome,"seu IMC é:",imc,"portanto vocé esta com \"OBESIDADE GRAU II\"")
else:
    print("senhor(a)",nome,"seu IMC é:",imc,"portanto vocé esta com \"OBESIDADE GRAU III (mórbida)\"")
print()
print("=="*20)
print("OBRIGADA, TENHA UM ÓTIMO DIA!".center(35))
print("=="*20)
