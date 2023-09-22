import math
def acima_da_media(lista):
    '''Retorna uma lista com as notas dos alunos que ficaram acima da média
    lista -> lista'''
    soma= sum(lista)
    quantidade_notas = len(lista)
    media = math.ceil(soma / quantidade_notas)
    novo_elemento = list.append(lista, media)
    crescente = list.sort(lista)
    indice = list.index(lista,media)
    lista_final = lista[indice+1:]
    return lista_final