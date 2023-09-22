def faltante(numeros):
    '''funcao que, dada uma sequencia de numeros, retorna o numero que esta faltando;
    list(int)->int'''
    posicao = 0
    while (numeros[posicao]<len(numeros)):
        if(numeros[posicao + 1] - numeros[posicao]==1):
            posicao = posicao + 1
            termo = numeros[posicao] + 1
        else:
            termo = numero[posicao]
    return termo