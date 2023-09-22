def conta_numero(numero,matriz):
    '''funcao que dado uma matriz e um numero inteiro retorna quantas vezes esse numero apareceu na matriz
    int,list->int'''
    for x in matriz:
        qtd=0
        for y in x:
            if y==numero:
                qtd=qtd+1
    return qtd