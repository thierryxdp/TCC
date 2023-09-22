def faltante(lista):
    """a lista eh colocada em ordem e buscamos encontrar o valor que falta
    diminuindo o valor posterior pelo anterior, ate encontrar um que o total
    nao seja 1
    list -> int"""
    lista.sort()
    i=0
    x=0
    if len(lista)==1 and lista[0]==1:
        return 2
    if lista[0]==1:
        while i<len(lista)-1:
            if lista[i+1]-lista[i] != 1:
                x=lista[i]+1
                if x not in lista:
                    return x
            else:
                x=lista[-1]+1
            i=i+1
    else:
        x=1
    return x