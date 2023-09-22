def media_matriz(matriz):
    '''
    	Dada uma matriz a função retorna a media da matriz 
        dada.
        list -> float
    '''
    soma = 0
    tamanho = 0
    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)
    return round(soma/tamanho,2)