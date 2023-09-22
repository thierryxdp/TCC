def eh_quadrada(matriz):
    """Recebe uma matriz e retorna um dado booleano que diz se a
matriz é quadrada ou não.
assinatura: list --> bool
testes:
eh_quadrada([[1,1,1], [2,2,2], [3,3,0]]) == True
eh_quadrada([]) == True
"""
    if len(matriz) == 0 or len(matriz) == len(matriz[0]):
        return True
    if not len(matriz) == len(matriz[0]):
        return False