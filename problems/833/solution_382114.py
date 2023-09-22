def conta_numero(numero,matriz):
    '''função que retorna a quantidade de vezes que um numero aparece na matriz'''
    '''int,matriz-->int'''
    cont=0
    for x in matriz:
        for num in x:
            if numero==num:
                cont=cont+1
    return cont