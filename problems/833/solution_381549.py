def conta_numero (numero, matriz):
    """Função que, dado um número e uma matriz, retorna quantas vezes o número aparece na matriz.
    Entrada: int e lista.
    Saída: int."""
    
    ocorrencias = ''
    i = 0
    j = 0
    
    while i < int(range(matriz)):
        while j < range(matriz[j]):
            if matriz[i][j] == str(numero):
            	ocorrencias = ocorrencias + 1
        	i = i+1
        	j = j+1
        
    return ocorrencias