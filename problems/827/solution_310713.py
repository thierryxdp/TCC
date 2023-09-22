def qtd_divisores(numero):
    '''A função conta os divisores de
    um numero dado como entrada.
    int --> int'''

    qtd = 0
    counter = 0

    while counter <= numero:
        if counter > 0:
            if numero % counter == 0:
                qtd += 1
        counter += 1

    return qtd