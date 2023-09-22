def conta_numero(numero,matriz):
    '''Funcao conta e retorna quantas vezes um numero aparece
    na matriz, int,list->int'''
    vezes=0
    for i in matriz:
        for j in i:
            if numero == j:
                vezes+=1
    return vezes