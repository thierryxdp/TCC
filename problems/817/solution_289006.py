def acima_da_media(lista):
    ''' Funcao que dada uma lista com notas de alunos, retorna uma lista
    	com as notas acima da media list >>> list'''
    media = sum(lista)/len(lista)
    lista.append(media)
    lista.sort()
    posicao_media = lista.index(media)
    return lista[posicao_media+1:]