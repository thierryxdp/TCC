def media_matriz (matriz):
    """Função que, dada uma matriz, retorna a média de todos os números da matriz
    Entrada: list.
    Saída: int."""
    
    soma = 0
    i = 0
    j = 0
    
    for i in range(0,len(matriz)):
    	for j in range(0,len(matriz[0])):
        	soma = soma + matriz[i][j]
            i = i + 1
            j = j + 1
            
    media = soma/(i*j)
    return media