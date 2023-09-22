def qtd_divisores(numero):
    """
    	Recebe um número e retorna sua quantidade de divisores.
        int --> int
    """
 	qtdDeDisores = 0
    divisor = 1
    while divisor <= numero:
        if numero%divisor == 0:
            qtdDeDisores += 1
      	divisor += 1
    return qtd