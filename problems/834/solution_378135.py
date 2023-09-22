def media_matriz(matriz:list)->float:
    '''Função que retorna a média de todos os números da matriz, com precisão de duas casas decimais.'''
    ind=0
    soma=0
    for i in matriz:
        soma=soma+sum(i)
        ind=ind+len(i)
    return round(soma/ind,2)