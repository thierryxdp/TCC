def faltante (lista):
    '''função que dada uma lista de números inteiros
    descubra e retorne qual número inteiro está faltando
    nesse intervalo.
    list -> int'''
    elemento = lista
    pos = 0
    numero_f = 0
    n = len(lista)
    while pos < len(lista) - 1:
        if ((elemento[pos+1] - elemento[pos]) > 1) and elemento[pos+1] > elemento[pos]:
            numero_f = elemento[pos] + 1
        elif ((elemento[pos] - elemento[pos+1]) > 1) and elemento[pos+1] < elemento[pos]:
            numero_f = elemento[pos] - 1
        pos += 1
    if numero_f == 0:  
        if elemento[1] > elemento[0] and elemento[0] == 1:
            numero_f = elemento[n-1] + 1
        elif elemento[1] > elemento[0] and elemento[0] != 1:
            numero_f = elemento[0] - 1
        elif elemento[0] > elemento[1] and elemento[n-1] == 1:
            numero_f = elemento[0] + 1
        elif elemento[0] > elemento[1] and elemento[n-1] != 1:
            numero_f = elemento[n-1] - 1
    return numero_f