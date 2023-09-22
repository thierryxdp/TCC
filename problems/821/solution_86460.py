def fatorial(numero):
    '''Funcao que calcula o taorial de um numero. 
    Exemplo: numero(5), resultado 5.4.3.2.1 
    int->int'''
    b=1
    a=1
    while a<=numero:
        b=b*a
        a = a + 1
    return b