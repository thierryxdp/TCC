def primo(n):
    """ Verifica se o número n é primo.
    	int -> bool
        
        Parameter:
        n: Número n.
        
        Returns:
        True se o número for primo, e False se o número não for.
    """
    lista = []
    for num in range(1, n + 1):
        if n % num == 0:
            lista.append(num)
    if len(lista) > 2:
        return False
    elif len(lista) == 2:
        return True