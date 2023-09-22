def faltante(lista=[]):
    '''função que dada ums lista descobre qual número
    no intervalo está faltando'''
    lista.sort()
    for i in range(len(lista)):
        if lista[i]!=i+1:
            return i+1
    return 0