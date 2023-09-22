def faltante(L,):
    """função que retorna qual peça está faltando em um quebra cabeça:list->int"""
    i=0
    b=(i+1)
    while i<=len(L):
        if L[0]!=1:
            return 1
        elif l[len(L)]!=(len(L)+1):
            return (len(L)+1)
        elif L[i]-L[b]!=(-1) or L[b]-L[i]!=1:
            return i+2
        i=i+1
        b=i+1