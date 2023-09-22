def eh_quadrada(matriz):
    """Recebe uma matriz e retorna um dado booleano que diz se a
matriz é quadrada ou não.
assinatura: list --> bool
testes:
"""
    if len(matriz) == len(matriz[0]) or len(matriz) == 0:
        return True
    if not len(matriz) == len(matriz[0]):
        return False