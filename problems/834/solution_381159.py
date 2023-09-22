def media_matriz (matriz):
    ''' calcula a media da matriz
list->float'''
    soma=0
    z=0
    for linha in matriz:
        for x in linha:
            soma += x
            z+=1
    return round(soma/(z),2)