def qtd_divisores(numero):
    """
    	Função que calcula quantos divisores tem o número 
        dado.
        int -> int
    """
    divisores = 0
    for x in range(numero+1):
        if numero%(x+1) == 0:
            divisores = divisores + 1
    return divisores