def qtd_divisores(numero):
    """
    	Função que calcula quantos divisores tem o número 
        dado.
        int -> int
    """
    divisores = 0
    for x in range(10):
        if numero%x == 0:
            divisores += 1
    return divisores