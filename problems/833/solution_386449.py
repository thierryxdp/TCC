def conta_numero(numero,matriz):
    '''função que conta a quantidade de vezes que um numero inteiro aparece na matriz
    int,list->int'''
    i=0
    contagem=0
    while i < len(matriz):
        contagem=contagem+list.count(matriz[i],numero)
        i=i+1
    return contagem