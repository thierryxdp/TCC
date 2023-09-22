def fatorial(num):
    '''Retorna o fatorial do
     número inserido; int->int'''
    contador=num
    fat=1
    while contador>0:
        fat=fat*contador
        contador=contador-1
    return fat