def media_matriz(matriz):
    """Função que, dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz com exatamente duas casas decimais de precisão
       list -> int"""
    soma = 0
    dividendo = 0
    for linha in matriz:
        for numero in linha:
            soma += numero
            dividendo += 1
    media = soma/dividendo
    return round(media,2)