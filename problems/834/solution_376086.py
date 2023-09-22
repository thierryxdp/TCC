def media_matriz(matriz):
    '''Dada uma matriz de inteiros não vazia, retorna a média de todos os numeros da matriz.
      matriz de int -> int'''
    soma = 0
    tamanho = 0
    for linha in matriz:
        
        soma += sum(linha)
        tamanho += len(linha)
    return round(soma/tamanho,2)