def eh_quadrada(matriz):
    '''Função que recebe uma matriz e identifica se ela é quadrada ou não.
    entrada da função: list
    saída da função: bool'''
    coluna = len(matriz[0])
    linha = len(matriz)
    
    return coluna == linha

    if len(matriz) == 0:
        return True