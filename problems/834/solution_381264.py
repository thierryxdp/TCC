def media_matriz(matriz):
    '''funcao que retorna dada uma matriz de inteiros não vazia, retorna a média de todos
os números da matriz
list->floar'''
    contagem=len(matriz)*len(matriz[-1])
    total=0
    for n in matriz:
        for termo in n:
            total=total + termo
    media= total/contagem
    return round(media,2)