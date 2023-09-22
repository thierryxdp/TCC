### Dada uma matriz não vazia m, esta função retorna a média de todos os números
### da matriz com 2 casas decimais de precisão.
### list(list) -> float

def calcular_soma_linha(m):
    soma = 0
    for i in range(len(m)):
            soma += m[i]
    return soma

def media_matriz(m):
    cont = len(m)*len(m[0])
    soma = sum(list(map(calcular_soma_linha,m)))
            
    return round(soma/cont,2)