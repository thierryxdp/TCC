def conta_numero(numero,matriz):
    '''funcao que dado uma matriz e um numero inteiro retorna quantas vezes esse numero apareceu na matriz
    int,list->int'''
    for x in range(len(matriz)):
        qtd=0
        for y in range(len([x])):
            if numero==y[x]:
                qtd=qtd+1
    return qtd