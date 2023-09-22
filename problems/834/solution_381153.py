def media_matriz (lista):
    ''' calcula a media 
list,int,str->float'''
    soma=0
    for linha in lista:
            soma += linha
    return soma/len(lista)