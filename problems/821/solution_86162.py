def fatorial(numero):
    '''Função que, dado um número, calcule seu fatorial; int->int'''
    listapramultiplicar = list(range(1,numero))
    contador=1
    fatorial=1
    while contador<=numero:
        fatorial=fatorial*contador
        contador=contador+1
    return fatorial