def faltante(lista):
    '''retorna qual peça está faltando de um número de peças de 1 a N
    list->int'''
    i=0
    s=0
    n=0
    soma = (((1+(len(lista)+1))*(len(lista)+1))/2)
    list.sort(lista)
    while i<len(lista):
        if sum(lista) != soma:
            s = (soma)-sum(lista)
        i = i+1
        n = i+1
    return n