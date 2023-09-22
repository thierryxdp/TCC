def media_matriz(matriz):
    """calcula e retorna a media de todos os elementos de uma matriz"""
quantidade=0
Soma_elementos=0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        Soma_elementos=elementos + matriz[i][j]
        quantidade=quantidade+1
media=Soma_elementos/quantidade
return round(media,2)