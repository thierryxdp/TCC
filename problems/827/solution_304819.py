def qtd_divisores(n):
    """ Conta quantos divisores o número n tem.
    	int -> int
        
        Parameter:
        n: Número n.
        
        Returns:
        Quantos divisores o número n tem.
    """
    lista = []
    for num in range(1, n + 1):
        if n % num == 0:
            lista.append(num)
    return len(lista)