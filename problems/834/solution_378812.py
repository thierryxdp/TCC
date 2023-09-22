def media_matriz(matriz):
    '''Funcao que, dada uma matriz de inteiros nao vazia, retorna a media de todos
os elementos da matriz com duas casas decimais de precisao.
List -> Float'''
    lin = len(matriz)
    col = len(matriz[0])
    soma = 0
    num_elementos = lin*col
    
    for i in range(lin):
        if sum(matriz[i]) != 0:
            soma += sum(matriz[i])
            
    media = soma/num_elementos
    return round(media,2)