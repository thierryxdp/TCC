def acima_da_media(notas):
    '''funcao que dada uma lista de notas, retorna uma lista com as notas que ficaram acima da media
       list -> list'''
    quant_notas = len(notas)
    media = (sum(notas)) / quant_notas    
    if (int(media) not in notas):
        list.append(notas, media)
        list.sort(notas)
        indice = list.index(notas, media)
        return notas[indice+1:]
    else:
        list.sort(notas)
        indice = list.index(notas, media)
        return notas[indice+1:]