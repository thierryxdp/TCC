'''Programa recebe uma matriz e determina se é quadrada. Caso 
seja quadrada, retorna True; e caso não seja, retorna False.
list -> bool'''
def eh_quadrada(matriz):
    proximo = 0
    acumulador = []
    while proximo < len(matriz):
        if len(matriz[proximo]) == len(matriz):
            acumulador = acumulador + [1]
        proximo = proximo + 1
    if len(acumulador) == len(matriz):
        return True
    else:
        return False