def busca(area, matriz):
    
    
    lista = []
    for i in range(len(matriz)):
    	if area in matriz[i][2]:
            matriz_encontrada = (matriz[i])
            list.remove(matriz_encontrada,area)
            list.append(lista,matriz_encontrada)
    return lista