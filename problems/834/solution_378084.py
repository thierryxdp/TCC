def media_matriz(matriz):
    """Função que ao receber uma matriz, retorna a média dos números
    dessa matriz, com duas casas decimais de precisão;
    list -> float"""
    media =0
    num_matrix=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            num_matrix.append(matriz[i][j])
            media = sum(num_matrix)/len(num_matrix)
    return round(media,2)