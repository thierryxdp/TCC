def maiores(lista1, n):
    list.append(lista1, n)
    list.sort(lista1)
    posicao_n=list.index(lista1, n)
    return lista1[(posicao_n+1):]
def acima_da_media(lista):
    '''Dada uma lista com as notas de uma turma, retorna a lista ordenada com as notas que ficaram acima da média
    list -> list'''
    media = sum(lista)/len(lista) * 1.05
    list.sort(lista)
    lista_maiores = maiores(lista, media)
    return lista_maiores