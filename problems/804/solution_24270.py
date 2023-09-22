'''Função que recebe uma tupla com 4 elementos e retorna apenas os que são pares'''
def filtra_pares(T):
    lista_T = []
    for n in T:
        if n%2 == 0:
            lista_T.append(n)
    return tuple(lista_T)