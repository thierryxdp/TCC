def qtd_divisores(numero):
    """
    Essa função conta quantos divisores um número possui
    Parametro de entrada: int
    Valor de Retorno: int
    """
    divisores = []
    for x in range(numero):
        if numero % x == 0:
        	list.append(divisores,x)
    return len(divisores)