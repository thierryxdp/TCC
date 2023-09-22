def qtd_divisore(inteiro):
    """
    Essa função dado um numero inteiro como entrada, ira retronar
    quantos divisores tal numero tem.
    int->int
    """
    divisor = 1
    qtd_divisores = 0
    for e in range(10):
        if e % divisor == 0:
            qtd_divisores += 1
        else:
            qtd_divisores = qtd_divisores
        divisor += 1
        
    return qtd_divisores