def acima_da_media(lista):
    """"Dada uma listas com as notas de alunos faz uma média e
    retorna uma nova lista com as notas acima da média."""
    lista.sort()
    media = sum(lista)/len(lista)
    return lista[int(media)+1:]