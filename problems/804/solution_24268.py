'''Função que recebe uma tupla com 4 elementos e retorna apenas os que são pares'''
def filtra_pares(T):
    lista_T = []
    for elemento in T:
        if elemento%2==0:
            lista_T.append(elemento)
    return tuple(lista_T)