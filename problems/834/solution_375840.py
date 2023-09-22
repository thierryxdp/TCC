def media_matriz (matriz):
    """Função que, dada uma matriz, retorna a média de todos os números da matriz
    Entrada: list.
    Saída: int."""
    
    for i in range(0,len(matriz)):
        soma = 0
        for j in range(0,len(matriz[0])):
            soma = soma + matriz[i][j]
    return soma