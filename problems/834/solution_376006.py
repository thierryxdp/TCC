#Questao3
def media_matriz(matriz):
    '''
    A função retorna a media de todos
    os valores.
    list -> float
    '''
    media = 0
    vezes = 0
    soma =0
    for l in range(len(matriz)):
        for c in range(matriz[l]):
            soma = soma + matriz[l][c]
            vezes = vezes + 1 
            media = round(soma/(vezes),2)

        return media