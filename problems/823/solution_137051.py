def faltante(L:list)->int:
    """função que descubra qual número inteiro do intervalo da lista está faltando"""
    i=1
    while i<len(L):
        if not L[i]-1 in L:
            return L[i]-1