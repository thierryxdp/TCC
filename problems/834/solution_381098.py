def media_matriz(matriz):
    '''dada uma matriz nao vazia a funcao
    retorna a media dos numeros da matriz
    matriz --> float'''
    soma_geral = 0
    quantidade_de_termos = len(matriz)*len(matriz[0])
    for i in matriz:
        for k in i:
            soma_geral += k
	return round(soma_geral/quantidade_de_termos,2)