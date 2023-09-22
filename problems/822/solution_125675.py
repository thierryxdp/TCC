def repetidos(lista):
    """retorna o número de vezes que um elemento da lista de entrada é igual ao elemento anterior; list -> int"""
    a=1
    b=0
    c=a-1
    while a<=len(lista):
        if lista[a]==lista[c]:
            b=b+1
        a=a+1
    return b