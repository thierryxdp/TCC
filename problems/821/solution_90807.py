def fatorial(numero):
    """
    funçao que dado um numero, calcula o fatorial dele.
    :param numero: int 
    :return: int 
    """
    contando = 1
    fatorial = 1

    while contando <= numero:
        fatorial *= contando
        contando += 1
        print(fatorial)

    return fatorial