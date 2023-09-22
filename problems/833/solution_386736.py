def conta_numero(numero,matriz):
    '''Dado um numero (numero-->int), e uma matriz (matriz), de quaisque tamanho conta e retorna quantas vezes o numero aparece na matriz'''
    cont=0
    for i in matriz:
        for j in i:
            if numero==j:
                cont=cont+1
        return cont