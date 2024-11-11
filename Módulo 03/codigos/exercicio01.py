"""
Programa para Calculo do Imposto de Renda retido na fonte
Author: Richard Brosler
Version: 2024-11-07
"""
from click import clear
clear()
# Variaveis de apoio
"""
Base de Cálculo (R$)	Alíquota (%)	Parcela a Deduzir do IR (R$)
Até 2.259,20*	              0	            0
De 2.259,21 até 2.826,65*	  7,5	        169,44
De 2.826,66 até 3.751,05	  15	        381,44
De 3.751,06 até 4.664,68	  22,5	        662,77
Acima de 4.664,68	          27,5	        896,00

"""
limite01, aliq01, ded01 = 2_259.20, 0, 0
limite02, aliq02, ded02 = 2_826.65, 7.5, 169.44
limite03, aliq03, ded03 = 3_751.05, 15, 381.44
limite04, aliq04, ded04 = 4_664.68, 22.5, 662.77
limite05, aliq05, ded05 = 4_664.69, 27.5, 896.00
ded_dep = 189.59
# Começando o programa
print("+" + "-" * 70 + "+")
print("|" + " " * 14 + "Programa para Calculo do Imposto de Renda " + " " * 14 +"|")
print("+" + "-" * 70 + "+")
salario = float(input("Digite o salário com dedução do INSS: "))
depentes = int(input("Digite número de dependentes: "))
# Calculando a Base do IR
base_ir = salario - depentes * ded_dep
# Verificando as faixas
if base_ir <= limite01:
    aliq, ded = aliq01, ded01
elif base_ir <= limite02:
    aliq, ded = aliq02, ded02
elif base_ir <= limite03:
    aliq, ded = aliq03, ded03
elif base_ir <= limite04:
    aliq, ded = aliq04, ded04
else:
    aliq, ded = aliq05, ded05
# Calculando o imposto
valor_ir = base_ir * aliq / 100 - ded
# Mostrando o imposto
print("Você vai pagar R$", valor_ir, " de IR.")