def acima_da_media (lista_numero):
    """função que dada uma lista com as notas dos alunos
    retorne uma lista em ordem com as notas que foram
    acima da média
    list , list"""
    lista = lista_numero
    media = sum(lista)/len(lista)
    list.append(lista, media)
    list.sort(lista)
    repeticoes = list.count(lista, media)
    if repeticoes ==1:
        indice = list.index(lista, media)
    else:
        indice = list.index(lista,media) + repeticoes -1
        return lista[indice+1:]