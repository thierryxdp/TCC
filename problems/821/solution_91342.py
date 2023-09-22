def fatorial(n):
    '''funcao que dado um numero calcula e retorna o fatorial
    deste numero.
    Parametro:
    int:
    Saida:float'''
    h= n-1
    while h>1:
        r=n*h
        h=h-1
    return r