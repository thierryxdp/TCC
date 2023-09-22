def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    lista1, lista2 = (L3 for t in zip(*sorted(zip(lista1, lista2))))
    return L3