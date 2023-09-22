def qtd_divisores0(numero):
    """essa função fornece a quantidade de divisores de um número
    a partir do próprio número.
    assinatura: int--->int"""
    soma=0
    for x in range(numero+1):
        if x==0:
            soma
        else:
            if numero/x == int(numero/x):
                soma=1+soma

    return soma