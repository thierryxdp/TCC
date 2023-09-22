def qtd_divisores(numero):
    '''retorna quantos divisores o numero indicado tem
    int -> int'''
    i = 1
    j = 0
    while i <= numero:
        if numero%i == 0:
            j += 1
            i += 1
        else:
            i += 1
    return j