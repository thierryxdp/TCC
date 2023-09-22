def fatorial(numero):
    '''funcao que dado um numero , calcula o fatorial deste numero'''
    i=2
    fatorial=1
    while i<=numero:
        fatorial=fatorial*i
        i= i+1
    return fatorial