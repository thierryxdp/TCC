def fatorial (numero):
    '''Função calcula o fatorial do numero.
    int -> int'''
    fat = 1
    numero_anterior = numero - (numero-1)
    while numero_anterior <= numero:
        fat = fat * numero_anterior
        numero_anterior = numero_anterior +1
    return fat