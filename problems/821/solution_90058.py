def fatorial(numero):
    '''Função que dado um número, calcula seu fatorial;
    str -> str'''
    resultado=1
    i=0
    while i<=numero:
        resultado*=i
        i+=1
    return resultado