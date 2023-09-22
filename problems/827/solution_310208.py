def qtd_divisores(numero):
    """
    	Recebe um número e retorna sua quantidade de divisores.
        int --> int
    """
    qtdDeDivisores = 0
    divisor = 1
    while divisor <= numero:
        if numero%divisor == 0:
            qtdDeDivisores += 1
        divisor += 1
    return qtdDeDivisores