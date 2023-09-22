def repetidos(lista):
    """função lê uma lista e conta quantas vezes um número é igual ao anterior. LIST(INT)->INT"""
    i=0
    repet=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            repet=repet+1
        i=i+1
    return repet