def media_matriz(m):
    '''Função retorna a média de todos os números de uma matriz
       list-->float'''
    soma=0
    for linha in m:
        soma+= sum(linha)
    media = soma/(len(m[1])*len(m))
    return round(media, 2)