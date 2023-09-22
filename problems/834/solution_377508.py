def media_matriz(matriz):
    '''função que recebe uma matriz de inteiros e retorna a 
    média de todos os seus números, com duas casas decimais.
    list -> float'''
    media=0
    for i in range(len(matriz)):
        mediadalinha=sum(matriz[i])/len(matriz[i])
        media=media+mediadalinha
    return round((media/len(matriz)),2)