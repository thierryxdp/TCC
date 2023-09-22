def conta_numero(numero, matriz):
    '''função que recebe como entrada uma matriz, em lista, de numeros inteiros
e como outra entrada recebe um numero inteiro, retorna o número de vezes que
o número inteiro da entrada aparaece na matriz; int,list(list)->int'''

    n=0

    for linha in matriz:
        for elemento in linha:
            if elemento==numero:
                n=n+1
    return n