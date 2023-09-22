def media_matriz(matriz):
    '''Dada uma matriz de inteiros não vazia, retorna a média de todos os números 
    da matriz. list(list)-> float''' 
    soma=0
    quantidade=0
 
    for linha in matriz:
        for elemento in linha:
            soma+= elemento 
            quantidade+=1
    return round(soma/quantidade,2)