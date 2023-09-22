def faltante(numeros):
    '''funcao que, dada uma sequencia de numeros, retorna o numero que esta faltando;
    list(int)->int'''
    posicao = 0
    if numeros[0]!=1:
        return 1
    elif posicao==len(numeros)-1 and numeros[0]==1:
        return numeros[posicao]+1
    elif posicao+1==len(numeros)-1:
        return numeros[posicao+1]+1
    else:
        while numeros[posicao]-numeros[posicao-1]==1:
            numeros[posicao] = numeros[posicao] + 1
        posicao=posicao + 1
        return numeros[posicao+1]+1