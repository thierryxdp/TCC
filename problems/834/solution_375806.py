def media_matriz(matriz):
    '''Função que dada uma matriz de inteiros não vazia, retorna a média de todos
os números da matriz, com uma precisão de duas casas decimais
    list -> float
    '''
    soma = 0
    termos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma+= matriz[i][j]
            termos+=1
    resposta = soma/termos
    return round(resposta,2)