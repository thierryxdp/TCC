def media_matriz(matriz):
    """ dada uma matriz de int não vazia retorna a média dos números da matriz 
    com aprox de 2 casas"""
    lista = []
    for i in range(len(matriz)):
        n=(sum(matriz[i]))/len(matriz[i])
        lista.append(n)
	qtd = len(lista)
    soma = sum(lista)
    return round(soma/qtd,2)