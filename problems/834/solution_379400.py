def numero_de_elementos_matriz(mat):
    linhas = len(mat)
    colunas = len(mat[0])
    return linhas * colunas
    

def soma_elementos_matriz(mat):
    c = 0
    for lin in mat:
        for e in lin:
            c = c + e
    return c

def media_matriz(mat):
    """Função que recebe uma matriz de números inteiros não vazia, 
    e retorna e retorna a média de todos os números da matriz com
    duas casas decimais de precisão.
    mat->float
    """
    return soma_elementos_matriz(mat)/numero_de_elementos_matriz(mat)