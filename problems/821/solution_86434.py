def fatorial (numero):
    '''Função calcula o fatorial do numero.
    int -> int'''
    fat = 1
    anterior = numero - (numero-1)
    while anterior <= numero:
        fat = fat * anterior
        anterior = anterior +1
    return fat