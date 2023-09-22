def fatorial(numero):
    '''funçao que calcula o fatorial de um numero'''
    fatorial = 1
    final = 1
    while final <= numero:
    fatorial *= final
    final += 1
    return fatorial