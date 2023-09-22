def faltante(numeros):
    '''funcao que, dada uma sequencia de numeros, retorna o numero que esta faltando;
    list(int)->int'''
    posicao = 0
    contador = 0
    if numeros[0]!=1:
        return 1        
    while posicao<len(numeros)-1:
        if numeros[posicao]+1==numeros[posicao+1]:
            contador=contador + 1
            posicao=posicao + 1
        else:
            contador=len(numeros)
    return numeros[posicao]+1