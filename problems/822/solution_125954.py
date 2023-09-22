def repetidos(lista):
    """Retorna o número de vezes que um elemento é igual
    ao anterior
    list->int"""
    i=0
    n=0
    while i<len(lista):
        if i == i+1:
            n=n+1
       	i=i+1
    return n