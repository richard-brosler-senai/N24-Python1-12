"""
Laboratório de exemplo de uso do input
author: Richard Brosler
version: 2024-11-06
"""
from click import clear
clear()
temp = input("Digite a temperatura atual em graus Celsius: ")
temp_fahr = float(temp) * 9 / 5 + 32
print("Temperatura em Fahrenheit é",temp_fahr)