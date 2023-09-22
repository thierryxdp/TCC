def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    L1 = lista1+lista2
    L2 = L1[:3:5]
    #1,2,3,4,5,6
    #6,2,7,5,9,1
    return L2