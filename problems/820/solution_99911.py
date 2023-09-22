def posLetra(s, n, i):
    '''função que a posição da ocorrência i de um n desejado 
    em s; str, str, int -> int'''
    k = 0
    acumulador = ''
    if str.count(s, n) < i:
        return -1
    while k < len(s):
        if len(acumulador) == i:
            return k
        elif s[k] == n:
            acumulador = acumulador + n
        k = k + 1