def faltante(lista=[]):
    '''função que dada ums lista de inteiros descobre 
    qual inteiro do intervalo está faltando'''
    lista.sort()
    for i in range(len(lista)):
        if lista[i]!=i+1:
            return 0