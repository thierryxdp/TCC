def media_matriz (lista):
    ''' calcula a media 
list,int,str->float'''
    soma=0
    y=0
    z=0
    for linha in lista:
        y+=1
        for x in linha:
            soma += x
            z+=1
    return soma/(y*z)