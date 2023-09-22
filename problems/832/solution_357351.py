def eh_quadrada(matriz):
    '''Funcao que verifica se a
    matriz dada e quadrada ou nao.
    Dados de entrada: list[list]
    Valor de saida: bool
    '''
    if len(matriz) != 0:
        return len(matriz) == len(matriz[0])
    else: 
        return True