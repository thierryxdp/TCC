def acima_da_media(lista):
    """"Dada uma listas com as notas de alunos faz uma média e
    retorna uma nova lista com as notas acima da média."""
    media = round(sum(lista)/len(lista),1)
    lista.insert(media,media)
    lista.sort()
    indice = lista.index(media)
    return lista[int(indice):]