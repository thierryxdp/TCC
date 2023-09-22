def faltante(lista):
    """
    list -> int"""
    lista.sort()
    i=0
    x=0
    while i<len(lista)-1:
        if lista[0]==1:
            if lista[i+1]-lista[i] != 1:
                x=lista[i]+1        
            else:
                x=lista[-1]+1
        else:
            x=1
        i=i+1
    return x