#list(int)->int
def faltante(lista):
    "função irá descobrir qual peça esta faltando no tabuleiro."
    contador=1
    x=0
    while contador in lista:
        contador= contador+ 1
    return contador