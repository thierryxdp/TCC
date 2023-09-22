def repetidos(lista):
    """verificamos se os elemento da lista e igual ao elemento anterior, se for
    acrescenta 1 ao valor do total, ao final da funcao obtemos o total de numeros
    repetidos.
    list -> int"""
    i=0
    t=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            t=t+1
        i=i+1
    return t