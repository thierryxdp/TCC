def eh_quadrada(matriz):
    """
    	Função que identifica se uma matriz é quadrada ou 
        não.
        list(list) -> bool
    """
    for linhas in len(matriz):
        for numeros in linhas:
            if not numeros:
                return False
        if len(linhas) == len(matriz):
            return True
        else: 
            return False