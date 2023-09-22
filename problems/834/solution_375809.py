def media_matriz(matriz):
    '''Função que dada uma matriz não vazia de inteiros retorna a média de todos os números dela.
    list(list) -> float'''
    
    contagem = []
    
    for linha in range (len(matriz)):
    	for coluna in range (len(matriz[0])):
            contagem.append(matriz[linha][coluna])
    return round(sum(contagem)/len(contagem))