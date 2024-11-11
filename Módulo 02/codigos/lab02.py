"""
Programa para calcular baskara
author: Richard Brosler
version: 2024-11-06
"""
from click import clear
# Limpando a tela
clear()
# Solicitando os lados a, b, c 
lado_a = float(input("Digite o valor do lado a: "))
lado_b = float(input("Digite o valor do lado b: "))
lado_c = float(input("Digite o valor do lado c: "))
# Calculando Delta
delta = lado_b ** 2 - 4 * lado_a * lado_c
# Calculando x1 e x2
x1 = ( -lado_b + delta ** (1/2) ) / ( 2 * lado_a )
x2 = ( -lado_b - delta ** (1/2) ) / ( 2 * lado_a )
# Mostrando x1 e x2
print("Valores de x1=",x1,",x2=",x2)