def media_matriz(m):
    """A função retorna a média de todos os números da matriz.
       list -> float"""
    media = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            list.append(media, m[i][j])
    return round(sum(media)/len(media), 2)
#Testes:
#m = [[1, 2, 3], [2, 3, 4]]
#media_matriz(m)--> 2.5

#m = [[5, 4, 3, 2], [0, 9, 8, 7]]
#media_matriz(m)--> 4.75

#m = [[0]]
#media_matriz(m)--> 0.0