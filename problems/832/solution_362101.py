def eh_quadrada(matriz):
    """ define se a matriz apresentada é quadrada ou não
    retorna o valor booleano"""
    tamanho = len(matriz)
    for i in range tamanho:
        for j in range tamanho:
            if tamanho == len(matriz[i]):
                return True
            else: