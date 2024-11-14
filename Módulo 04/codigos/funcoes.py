"""
Funções úteis para os programas em python
Author: Richard Brosler
Version: 2024-11-13
"""
from click import clear
"""
Função titulo
"""
def titulo(tit = "Programa Principal",colunas = 70):
    
    if len(tit) % 2 == 1:
        tit += " "
    
    esp = " " * ( ( colunas - len(tit) ) //2 )
    print("+" + "-" * colunas + "+")
    print("|" + esp + tit + esp + "|")
    print("+" + "-" * colunas + "+")

if __name__ == '__main__':
  clear()
  titulo()
