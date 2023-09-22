def eh_quadrada(matriz):
    '''Recebe uma matriz e retorna verdadeiro se for
    quadrada e falsa se não for.
    Retorno Booleano.'''
    for i in matriz:
        #Verifica se o número de linhas é o mesmo que o de colunas
        if len(matriz) != len(i):
            return False
    #se não der falso significa que é quadrada
    return True