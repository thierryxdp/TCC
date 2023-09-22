def  qtd_divisores(numero):
    """Funcao que definea quantidade de divisores um numero tem.
    int->int"""
    div = 1
    quant = 0
    while div <= numero:
        if numero%div==0:
            quant = quant + 1
        div = div + 1
    return quant