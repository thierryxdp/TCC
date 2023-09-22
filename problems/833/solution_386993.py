def conta_numero(numero,matriz):
    '''função que recebe um numero inteiro e uma matriz, conta e retorna quantas vezes o numero aparece na matriz.
    int,list -> int'''
    c=0
    for lin in matriz:
        for col in lin:
            if numero==col:
                c=c+1
    return c

# testes
#