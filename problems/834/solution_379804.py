def soma(mat):
    c=0 
    for lin in mat:
        for e in lin:
            c=c+e
    return c

def n_elementos(mat):
    c=0
    for lin in mat:
        for col in lin:
            c=c+1
    return c

def media_matriz(mat):
    '''funcao que dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz
    list -> float
    explicação: basta identificarmos a soma da matriz e os elementos, dividirmos e arredondarmos'''
    return round(soma(mat)/n_elementos(mat),2)