'''Função que recebe uma tupla com 4 elementos e retorna apenas os que são pares'''
def filtra_pares(tupla):
    lista_tupla = []
    for elemento in tupla:
        if elemento%2==0:
            lista_tupla.append(elemento)
    return tuple(lista_tupla)