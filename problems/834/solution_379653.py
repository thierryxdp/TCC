#Questao 3
def media_matriz(matriz):
    '''
    Funcao que dada uma matriz de inteiros nao vazia, retorna a media dos numeros da matriz.
    list->float.
    '''
    soma=0
    count =0
    for i in range(len(matriz)):
        
            soma += matriz[i][j]
            count += 1
            x = soma/count
                
    return round(x,2)