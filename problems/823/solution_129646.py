"""Recebe uma lista de numeros inteiros de 1 a N, em ordem e retorna o número
que está faltando
list -> int"""

def faltante(lista):
    i = 0
    falta = 0
    while i < len(lista):
        if lista[i] - lista[i-1] != 1:
            falta = falta + lista[i] - 1
        i = i + 1
    lista.append(falta)
    lista.sort()
    return lista