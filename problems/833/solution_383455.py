def conta_numero(numero, matriz):
    """ Conta quantas vezes o número aparece na matriz.
    	int -> int
        
        Parameters:
        numero: Número.
        matriz: Matriz.
        
        Returns:
        Quantas vezes o número aparece na matriz.
    """
    lista = []
    i = 0
    j = 0
    while i < len(matriz):
        while j < len(matriz[0]):
            if matriz[i][j] == numero:
                lista.append(matriz[i][j])
            j = j + 1
        i = i + 1
    return len(lista)