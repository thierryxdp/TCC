def acima_da_media(nota):
    '''funçao que dada a lista de entrada com as notas, retorna os números maiores que a media dos números da lista''' 
    '''list->list'''
    soma=sum(nota)
    Ni=len(nota) 
    media=(soma//Ni) 
    list.append(nota,media)
    list.sort(nota)
    list.reverse(nota)
    i=list.index(nota,media)
    lista=nota[0:i]
    list.sort(lista)
    return lista