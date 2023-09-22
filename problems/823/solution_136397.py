def faltante(lista):
    '''dada uma lista com n-1 inteiros descobre o numero inteiro faltando'''
    n=1
    retorno=[]
    while n<len(lista)+1:
        if n not in lista:
            return n
        n += 1
    return n