def qtd_divisores(numero):
    '''conta quantos divisiores o numero inserido tem; int -> int'''

    cont = 0
    
    for i in range(1,numero+1):
        if numero%i == 0:
            cont = cont + 1

    return cont