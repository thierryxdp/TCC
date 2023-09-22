def acima_da_media(lista):
    """"Dada uma listas com as notas de alunos faz uma média e
    retorna uma nova lista com as notas acima da média."""
    media = sum(lista)//len(lista)
    if media in lista:
        lista.sort()
        indice = float(lista.index(media))
        return int(lista[indice+1:])