import math
def acima_da_media(lista):
    '''Retorna uma lista com as notas dos alunos que ficaram acima da média
    lista -> lista'''
    soma= sum(lista)
    quantidade_notas = len(lista)
    media = math.ceil(soma / quantidade_notas)
    novo_elemento = list.append(lista, media)
    crescente = list.sort(lista)
    lista_final = lista[media+1:]
    return lista_final