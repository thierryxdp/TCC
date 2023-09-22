def acima_da_media(n):
    '''Funcao que calcula e retorna uma nova lista ordenda com as notas que ficaram acima da media.
    list,float->float,list'''
    for i in numeros:
        if i > n:
            return list(i)