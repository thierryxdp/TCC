def media_matriz(matriz):
        #Dada uma matriz, calcula a média de todos os valores dessa matriz.
        #entrada: matriz ; saida: media, com duas casas decimais
        media = 0
        soma = 0
        quant = 0
        for i in range(0, len(matriz)):
                for o in range(0, len(matriz[i])):
                        quant += 1
                        soma += matriz[i][o]
                        media = soma / quant

        return round(media, 2)