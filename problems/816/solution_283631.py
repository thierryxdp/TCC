def maiores(lista_numero,n):
    '''dado uma lista de numeros inteiros e um numero n;
    temos como volta uma lista que contem apenas os numeros
    maiores que n, ademais com a sua ordem crescente de termos'''
    x=insere(lista_numero,n)
    posicaoDeN=list.index(x,n)
    return x[posicaoDeN+1:]