def eh_quadrada(matriz):
    """Recebe uma matriz e retorna um dado booleano que diz se a
matriz é quadrada ou não.
assinatura: mat --> bool
testes:
"""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                return True
            if i != j:
                return False