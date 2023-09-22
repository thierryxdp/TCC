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
    for i in matriz:
        for j in matriz[i]:
            if matriz[i][j] == numero:
                lista.append(matriz[i][j])
    return len(lista)