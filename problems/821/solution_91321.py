def fatorial(num):
    '''Recebe como entrada um número inteiro e retorna 
    o seu fatorial.
    int -> int'''
    contador=num
    acumulador=1
    while contador>1:
        acumulador=acumulador*contador
        contador=contador-1
    return acumulador