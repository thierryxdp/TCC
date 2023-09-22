def media_matriz(matriz):
    '''calcula e retorna a media de todos os elementos da matriz apresentada
    list-> float'''
    soma=[]
    for linha in matriz:
        for num in linha:
            soma+=[num]
    media=sum(soma)/(len(matriz)*len(matriz[0]))
    return round(media,2)