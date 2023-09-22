def numero = int(input("Digite um numero")):
    """XXXXXXX"""
    divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            divisores = divisores + 1
            if divisores > 1:
    if divisores > 1:
        return True
    else:
        return False