def media_matriz(x):
    """Função que retorna a média de todos os numeros da matriz
    list--> int"""
    elementos=len(x)*len(x[0]);
    b=0;
    for i in range(len(x)):
        for j in range(len(x[0])):
            b=b+a[i][j]
    media=b/elementos;
    return round(media,2)