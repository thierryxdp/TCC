from random import randint
def faltante(lista):
    ''' função que, dada uma lista com N − 1 inteiros numerados de 1 a N, descubra qual número inteiro deste intervalo está faltando.
    Entrada: list;
    Saída: int'''
    var1 = lista[-1]
    var2 =list(range(var1))
    numero= randint(1,var1)
    while numero in var2:
        var2 =list(range(var1))
    return numero