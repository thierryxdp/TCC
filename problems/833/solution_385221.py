def conta_numero(matriz,inteiro):
    '''função que recebe como entrada uma matriz, em lista, de numeros inteiros
e como outra entrada recebe um numero inteiro, retorna o número de vezes que
o número inteiro da entrada aparaece na matriz; list(list),int->int'''

    n=0

    for linha in matriz:
        for elemento in linha:
            if elemento==inteiro:
                n=n+1
    return n