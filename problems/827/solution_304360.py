def qtd_divisores(numero):
    """A função calcula quantos divisores um numero tem;
    int -> int"""
    divisores = 0
    i = 1
    
    if numero < 0:
        numero *= -1
    
    while i <= numero:
        if numero%i == 0:
            divisores += 1
        i = i + 1
    return divisores