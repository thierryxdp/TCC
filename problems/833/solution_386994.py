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
# conta_numero(8,[[5,6,7,8]])
# saida esperada: 1
# conta_numero(7,[[2,3,4],[0,2,3]]
# saida esperada: 0