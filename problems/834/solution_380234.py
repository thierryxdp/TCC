def media_matriz(matriz):
    """Função que dada uma matriz não vazia, retorna a média de todos os número com duas casas decimais de precisão;
    list(list) -> float"""
    
    soma = 0
    
    for lista in matriz:
        for numero in lista:
            soma = soma + numero
            
    return soma/len(matriz)*len(matriz[0])