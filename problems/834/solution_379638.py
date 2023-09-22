def num_da_matriz(matriz):
    '''Dado as matrizes multiplica o número de seus elementos'''
    l=len(matriz)
    c=len(matriz[0])
    return l*c

def soma(matriz):
    '''Dado a matriz soma o valor de seus elementos'''
    soma=0
    for l in matriz:
        for c in l:
            soma=soma+c
    return soma

def media_matriz(matriz):
    '''Dado a matriz(matriz), retorna a media de todos os números contidos na mesma'''
    return round(soma(matriz))/(num_da_matriz(matriz))