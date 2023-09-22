def conta_numero(numero, matriz):
    '''dado um número inteiro retorna quantas vezes'''
    '''int,list->int'''
    qt=0
    for numeros in matriz:
        for i in numeros:
            if i == numero:
                qt+=1
    return qt