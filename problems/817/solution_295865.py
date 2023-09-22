def acima_da_media(notas):
    '''
    '''
    media = sum(notas) / len(notas)
    nova_lista = notas.append(media)
    nova_lista.sort()
    indice = nova_lista.index(media)
    return nova_lista[indice+1:]