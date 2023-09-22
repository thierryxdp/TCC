def conta_numero(numero, matriz):
    '''Função que recebe um número inteiro e uma matriz de inteiros
    de qualquer tamanho, conta e retorna quantas vezes esse número apareceu 
    naquela matriz.
    tipo de entrada: int e list
    tipo de saída: int'''
    coluna = len(matriz[0])
    linha = len(matriz)
    if numero in linha:
        return