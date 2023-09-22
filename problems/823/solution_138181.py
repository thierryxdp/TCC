def faltante(L):
    '''
    funcao que recebe uma lista L, que contem
    numeros inteiros nao repetidos que vao de 1
    a N, e descobre e retorna qual numero inteiro
    desse intervalo esta faltando
    list->int
    '''
    x = 0
    lista=sorted(L)
    while x<len(L):
        if x+1==lista[x]:
            x=x+1

        else:
            return x+1

    return x+1