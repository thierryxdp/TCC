def faltante(lista):
    '''Funcao que, dada uma lista, retorna o numero que esta faltando'''
    i = 0
    num_faltante = 0 
    lista.sort()
    while i<=len(lista):
        if (lista[i+1] - lista[1]) != 1:
            num_faltante = (lista[i+1] + lista[1])/2
        i = i + 1
        if num_faltante == 0 and lista[0] == 1:
            num_faltante = lista[-1]+1
        if num_faltante == 0 and lista[0] != 1:
            num_faltante = 1
    return num_faltante