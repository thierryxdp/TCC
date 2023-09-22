def eh_quadrada (matriz):
    """ A função eh_quadrada identifica se uma matriz é quadrada ou nao. Observação: uma matriz vazia (sem nenhuma linha nem coluna) é considerada quadrada.
        
        Parameters:
        matriz = matriz a ser analisada

        Testes:
            eh_quadrada ([[1,2],[3,4]]) == True
            eh_quadrada ([]) == True
            eh_quadrada ([[1,2]]) == False
            eh_quadrada ([[1],[2]]) == False

        Returns:
            True se a matriz for quadrada e false se não for.
            list --> bool
    """
    if len(matriz) == 0:
        return True
    else:
        return len(matriz) == len(matriz[0])