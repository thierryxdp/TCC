def fatorial(numero):
    ''' Função  que dado um numero, calcule o fatorial
    deste numero;
    int -> int'''
    i = 1
    s = 1
    while i<=numero:
        s = s*i
        i += 1
    return s