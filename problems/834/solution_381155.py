def media_matriz (lista):
    ''' calcula a media 
list,int,str->float'''
    soma=0
    for linha in lista:
        for x in linha:
            soma += x
    return soma/len(lista[0])