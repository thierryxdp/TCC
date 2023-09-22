def acima_da_media(lista):
    """"Dada uma listas com as notas de alunos faz uma média e
    retorna uma nova lista com as notas acima da média."""
    media = sum(lista)/len(lista)
    lista.insert(4,media)
    lista.sort()
    indice = lista.index(media)
    return lista[indice+1:]