def faltante(L,):
    """função que retorna qual peça está faltando em um quebra cabeça:list->int"""
    i=0
    b=(i+1)
    while i<len(L):
        if L[b]-L[i]!=1 or L[i]-L[b]!=1:
            return i
        i=i+1
        b=i+1