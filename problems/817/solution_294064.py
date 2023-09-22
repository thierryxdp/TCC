import math
def acima_da_media(lista):
    '''Retorna uma lista com as notas dos alunos que ficaram acima da média
    lista -> lista'''
    copy = lista[:]
    soma= sum(lista)
    quantidade_notas = len(lista)
    media = round(soma / quantidade_notas)
    novo_elemento = list.append(lista, media)
    crescente = list.sort(lista)
    indice = list.index(lista,media)
    if media not in copy:
        return  lista[indice+1:]
    else:
        return  lista[indice+2:]