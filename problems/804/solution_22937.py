"""Retorna apenas os elementos pares da tupla inicial escolhida
assinatura: int, int, int, int -> int"""

def filtra_pares(tupla):
    list_final = list()
    for x in tupla:
        if x % 2 == 0:
            list_final += [x]
            
    tuple_final = tuple(list_final)
    return tuple_final