def faltante(lista):
    '''A partir de uma lista com N-1 inteiros numerados de 1 a N;
retorna qual numero desse intervalo está faltando;
list => int'''
    n = list(range(len(lista)+2))
    i = 1
    x = []
    while len(lista)+2>i:
        if n[i] not in lista:
            x = x + [n[i]]
        i = i+1
    return int(''.join(map(str,x)))