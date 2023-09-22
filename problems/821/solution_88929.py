def fatorial(n):
    '''Funcao recebe um numero e retorna o fatorial desse mesmo numero
int -> int'''
    primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,71,73,79,83,89,97]
    fator = 0
    contador = 0
    while (n != 1):
        if (n%primos[contador] == 0):
            fator = primos[contador]
            n = 1
        contador += 1
    return fator