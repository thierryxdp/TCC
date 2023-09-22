def faltante(l):
    ''' Função que analisa uma lista l que contem a identificação das peças
    de um quebra-cabeças e informa que peça falta.
    list->int'''
    i=0
    n=len(l)
    z=list(range(1,n))
    while i<(n-1):
        list.remove(z,l[i])
        i=i+1
    x=len(z)
    return z[:]