def fatorial(numero):
    """
    funcao qur dado um numero retorna seu fatorial.
    :param numero: int 
    :return: int 
    """
    contando = 1
    fatorial = 1

    while contando <= numero:
        fatorial *= contando
        contando += 1

    return fatorial