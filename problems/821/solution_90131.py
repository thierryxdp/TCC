def fatorial(num):
    '''dado um ńumero, calcula o fatorial deste ńumero.''' 
    numero = num

    resultado=1
    count=1

    while count <= numero:
        resultado *= count
        count += 1

    return resultado