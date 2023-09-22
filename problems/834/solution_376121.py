def media_matriz(m):
    """Dado uma matriz de inteiros, a função retorna a média de todos os números da matriz com duas casas de precisão;
    list[list...]->float"""
    total=0
    divisor=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            total=total+m[i][j]
            divisor=divisor+1
    resultado= round(total/divisor,2)
    return resultado