import math
def maiores(lista_inteiros, n):
    '''crie uma função que, dada uma lista de números inetiros e um número inteiro n, retorne unma nova lista que contenha os números da lista orginal maiores que n ordenados de forma crescente.list,int-->list.'''
    list.insert(lista_inteiros, 0, n)
    list.sort(lista_inteiros)
    lista = list.index(lista_inteiros, n)
    return lista_inteiros[lista + 1:]

def acima_da_media(notas):
    '''crie uma funcao que, dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média. list-->list.'''
    media = math.ceil((sum(notas))/(len(notas)))
    if len(notas) <= 1:
        return []
    else:
        return maiores(notas, media+1)