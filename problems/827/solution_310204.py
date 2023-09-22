def qtd_divisore(numero):
    """
    	Recebe um número e retorna sua quantidade de divisores.
        int --> int
    """
 	qtd = 0
    divisor = 1
    while divisor <= numero:
        if numero%divisor == 0:
            qtd += 1
      	divisor += 1
    return qtd