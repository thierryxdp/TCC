def eh_quadrada(matriz):
    '''Recebe uma matriz e identifica se ela é quadrada ou não, ou seja,
    se ela possui o mesmo número de linhas e de colunas.

    obs: uma matriz vazia (sem nenhuma linha nem coluna) ́e considerada
    quadrada.

    list -> bool'''

    numLinhas = len(matriz)

    if numLinhas == 0:
        return True
    
    numColunas = len(matriz[0])

    return numLinhas == numColunas