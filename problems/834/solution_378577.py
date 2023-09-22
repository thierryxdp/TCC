def media_matriz(matriz):
        # Função que dada uma matriz, calcula a media dos números
        # list -> float
        soma = 0
        divisor = 0
        media = 0
        for i in range(len(matriz)):
        	for counter in range(len(matriz[i])):
            	divisor += 1
                soma += matriz[i][counter]
                media = soma / divisor
        return round(media, 2)