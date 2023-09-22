import math
def media_matriz (matriz):
    ''' dado um numero inteiro e uma matriz qualquer contendo apenas inteiros
    retorna quantas vezes o numero aparece ao longo da matriz
    int, list(list) --> int '''
    
    media = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(media, matriz[i][j])
            
	return round(sum(media)/len(media),2)