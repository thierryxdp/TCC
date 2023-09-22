def filtraMultiplos(lista,n):
    """Filtra os múltiplos de um número n e retorna uma lista com tais múltiplos.
    list,int->list"""
    c=0
    L=[]
    while c<len(lista):
        if lista[c]%n==0:
            L = L + [lista[c]]
        c = c + 1
    return L