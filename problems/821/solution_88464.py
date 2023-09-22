def fatorial(numero):
    '''Função que dado um número, calcule o fatorial deste número; int->int'''
    ind=1
    f=1
    while ind<=numero:
        f=f*ind
        ind=ind+1
    return f