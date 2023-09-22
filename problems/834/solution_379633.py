def num_da _matriz(matriz):
    l=len(matriz)
    c=len(matriz[0])
    return l*c

def soma(matriz):
    soma=0
    for l in matriz:
        for c in l:
            soma=soma+c
    return soma

def media_matriz(matriz):
    '''Dado a matriz(matriz), retorna a media de todos os números contidos na mesma'''
    return round(soma(matriz))/(num_da_matriz(matriz),2)