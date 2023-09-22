def media_matriz(matriz):

        linhas = len(matriz)

        colunas = len(matriz[0])

        numeros = linhas*colunas

        media_por_termos = lambda termo: termo/numeros

        matrizmap = []

        saida = 0

        for linha in matriz:

                matrizmap.append(list(map(media_por_termos, linha)))

        for linha in matrizmap:

                for elemento in linha:

                       saida += elemento

        return round(saida, 2)