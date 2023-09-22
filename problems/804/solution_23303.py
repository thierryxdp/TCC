"""Função que dada uma tupla com 4 elemento, retonara uma nova tupla com apenas números pares, porem se não huver números pares na tupla original ira retornar uma nova tupla vazia.
Casos teste:
(25,36,98,65) == (36,98)
(25,85,96,31) == (96)
(1,3,6,8) == (6,8)
assinatura: tuple -> tuple"""
def filtra_pares(t):
    lista = []
    if len(t) == 4:
        if t[0]%2 == 0:
            lista.append(t[0])
        if t[1]%2 == 0:
            lista.append(t[1])
        if t[2]%2 == 0:
            lista.append(t[2])
        if t[3]%2 == 0:
            lista.append(t[3])
    else:
        return()
    return(tuple(lista))