def faltante(lista):
    '''Recebe uma lista com um intervalo incompleto de numeros inteiros e
       retorna o faltante deste intervalo.
       list -> int'''
    i = len(lista)-1
    while i >= 0:
        if lista[i] - lista[i-1] > 1:
            return lista[i]-1
        else:
            i = i - 1
    else:
        if lista[0] > 1:
            return 1
        elif lista[0] == 1:
            return len(lista)+1