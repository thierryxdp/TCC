def acima_da_media(numeros):
    '''Funcao que calcula e retorna uma nova lista ordenda com as notas que ficaram acima da media.
    list,float->float,list'''
    media=sum(numeros)/len(numeros)
    list.append(numeros,media)
    list.sort(numeros)
    return[i for i in numeros if i > media]