def media_matriz(matriz: list[int])->int:
    """Função que, dada uma matriz de inteiros não vazia, retorna a média
    de todos os números da matriz."""
    
    for i in matriz:
        for j in matriz[i]:
            soma = list(map(sum(matriz[i]), matriz))
            
    return soma