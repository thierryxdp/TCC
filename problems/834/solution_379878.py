def media_matriz(matriz):
    
    '''Função que, dada uma matriz de inteiros,
    retorna a media de todos os numeros da mesma.
    
    :param matriz:list
    :return:float'''
    
    soma = 0
    tamanho=0
    for linha in matriz:
        soma=soma+sum(linha)
        tamanho=tamanho+len(linha)
    
    return soma/tamanho