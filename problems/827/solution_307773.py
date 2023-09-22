qtd_divisores(num):
    """
    	Função que calcula quantos divisores tem o número 
        dado.
        int -> int
    """
    divisores = []
    for x in range(10):
        if x%num == 0:
            list.append(divisores,x)
    return divisores