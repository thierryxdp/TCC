# Dada uma matriz não vazia m, esta função retorna a média de todos os números
# da matriz com 2 casas decimais de precisão.
# list(list) -> float

def media_matriz(m):
    cont = len(m)*len(m[0])
    soma = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            soma += m[i][j]
            
    return round(soma/cont,2)