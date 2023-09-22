def fatorial(numero):
    '''funcao que dado um numero calcule o fatorial deste numero
    int->int'''
    x=1
    while numero>0:
        x*=numero
        numero=numero-1
    return x