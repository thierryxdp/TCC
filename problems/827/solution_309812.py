def qtd_divisores(numero):
    """essa função fornece a quantidade de divisores de um número
    a partir do próprio número.
    assinatura: int--->int"""
    soma=0
    for x in range(1,numero+1):
        if numero/x == int(numero/x):
            soma=1+soma

    return soma