def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    L1 = [lista1]
    L2 = [lista2]
    return [L1[:1], L2[:1], L1[1:2], L2[1:2], L1[2:], L2[2:]]