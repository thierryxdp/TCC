def nums_da_matriz(matriz):
    '''Função que calcula o total de números de uma dada matriz, matriz>>int'''
    linhas= len(matriz)
    colunas=len(matriz[0])
    return (linhas*colunas)

def soma(matriz):
    '''Função que soma os números da matriz, matriz>>int'''
    soma= 0
    for s in range(len(matriz)):
        for u in range(len(matriz[s])):
            soma= soma+ matriz[s][u]
        return soma
    
def media_matriz(matriz):
        '''Função que calcula a média de uma dada matriz'''
        return round(( soma(matriz)/ nums_da_matriz(matriz)),2)