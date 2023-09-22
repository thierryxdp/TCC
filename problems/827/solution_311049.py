def qto_divisores(n):
    '''funcao dado um numero retorna o por quantos numero esse numero é divisive
    int -> int'''
    divisores = []
    contador = 1
    while numero >= contador:
        resto = numero % contador
        if resto == 0:
            divisores += [contador]
            contador += 1
        else:
            contador += 1
    return len(divisores)