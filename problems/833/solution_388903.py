def conta_numero(n,matriz):
    '''Recebe um numero inteiro e uma matriz e retorna quantas vezes
    este inteiro aparece na matriz;
    int,list->int'''
    quantidade = 0
    for i in matriz:
        quantidade = quantidade + list.count(i,n)
    return quantidade