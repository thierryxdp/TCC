"""Recebe uma lista de números e retorna a qnt de vezes que um elemento é 
igual ao seu anterior
list -> int"""

def repetidos(lista):
    i = 0
    qnt = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            qnt = qnt + 1
        i = i + 1
    return qnt