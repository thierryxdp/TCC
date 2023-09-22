def faltante(lista):
    '''função que certos números descubra qual número no intervalo esta faltando; list => int'''
    n=1
    retorno=[]
    while n<len(lista)+1:
        if n not in lista:
            return n
        n += 1
    return n