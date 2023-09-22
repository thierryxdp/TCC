def conta_numero(numero,matriz):
    '''Retorna quantas vezes um numero aparece numa matriz.
    int,matriz->int'''
    soma=0
    for i in matriz:
        for j in i:
            if numero==j:
                soma+=1
    return soma