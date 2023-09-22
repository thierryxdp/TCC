def faltante(numeros):
    '''funcao que, dada uma sequencia de numeros, retorna o numero que esta faltando;
    list(int)->int'''
    posicao = 0
    if posicao<len(numeros):
        while numeros[posicao] - numeros[posicao-1]==1:
            posicao = posicao + 1
    return numeros[posicao] + 1