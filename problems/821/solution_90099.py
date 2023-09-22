def fatorial(numero):
    '''retorna o fatorial do número mencionado.
    int -> int'''
    cont = 1
    fat = 1

    while cont <= numero:
        fat = fat * cont
        cont = cont + 1

    return fat