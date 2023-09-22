def faltante(lista):
    '''Recebe umas lista com N-1 inteiros numerados de 1 a N, e descobre qual inteiro deste intervalo está faltando
    list -> int'''
    i=0
    j=2
    x=1
    list.sort(lista)
    while j < len(lista):
        if lista[i] != lista[j]-2:
    return x
        else:
            i = i + 1
            j = j + 1
            x = x + 1