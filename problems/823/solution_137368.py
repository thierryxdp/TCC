def faltante(lista):
    ''' função que entrega o número n de peças de um
        quebra cabeças através de uma lista com valor N-1.
        list ---> int '''
    a = 1
    n = len(lista) - 1
    while a != len(lista) + 2:
        if a not in lista and a < lista[n]:
            return a
        if a not in lista and a > lista[n]:
            return a
        if a in lista:
        	a += 1