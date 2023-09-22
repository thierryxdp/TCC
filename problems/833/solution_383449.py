def conta_numero(numero,matriz):
    """Dá quantas vezes um número aparece em uma matriz
    	int, list -> int
        Parameters:
        número: Número a ser encontrado
        matriz: Matriz na qual o número vai ser procuraod
        
        Returns:
        A quantidade de vezes que o número aparece na matriz dada
    """
    
    contador = 0
    
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if matriz[i][j] == numero:
                contador = contador + 1
                
    return contador