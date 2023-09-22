def media_matriz(matriz):
    '''Retorna a média de todos os números da matriz de inteiros não
    vazia dada, com 2 casas decimais de precisão; list -> float'''
    soma=0
    termos=0
    for i in matriz:
        for j in i:
            soma=soma+i
            termos=termos+1
	media=soma/termos
    return media