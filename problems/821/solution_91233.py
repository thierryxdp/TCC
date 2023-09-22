def fatorial (n):
    """essa função, dada como parametro um numero, calcule o fatorial deste numero
    int->int"""
    proximo=1
    num=n
    while proximo < n:
        num=num*proximo
        proximo=proximo+1
    return num