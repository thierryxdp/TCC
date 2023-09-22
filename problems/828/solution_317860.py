def primo (numero):
    """
    Essa função verificca se o número  é primo
    Parametro de entrada: int
    Valor de Retorno: int
    """
    divisores = []
    for x in range(numero):
        if numero % (x+1) == 0:
            list.append(divisores,x)
    return (len(divisores))==2