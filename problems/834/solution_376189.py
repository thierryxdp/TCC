def media_matriz(matriz):
    lista = []
    linha = len(matriz)
    for x in range(0,linha):
        coluna = len(matriz[x])
        media = (sum(matriz[x]))/coluna
        lista.append(media)
    	media2 = (sum(lista))/len(lista)
   	return media2