def num_da_matriz(matriz):
    '''função que calcula a quantidade de números de uma matriz'''
    l= len(matriz)
    c= len(matriz[0])
    return c*l

def soma(matriz):
    '''Função que soma os elementos de uma dada matriz'''
    soma= 0
    for i in matriz:
        for j in matriz[i][j]:
            soma= soma + matriz[i][j]
        return soma
    
def media_matriz(matriz):
    '''função que calcula e retorna o valor da média de uma dada matriz'''
    return round((soma(matriz)/num_da_matriz(matriz)),2)