def conta_numero (numero, matriz):
    """Função que, dado um número e uma matriz, retorna quantas vezes o número aparece na matriz.
    Entrada: int e lista.
    Saída: int."""
    
    ocorrencias = ''
    i = 0
    j = 0
    
    while i < len(matriz):
        while j < len(matriz[j]):
            if matriz[i][j] == numero:
            	ocorrencias = ocorrencias + 1
        i = i+1
        j = j+1
        
    return ocorrencias