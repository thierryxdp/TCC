def conta_numero(numero,matriz):
    '''dado um numero inteiro e uma matriz com numeros inteiros, essa funcao conta e retorna 
    quantas vezes esse numero aparece na matriz
    int,list-->int'''
    contagem=0
    for i in matriz:
        contagem+=list.count(i,numero)
    return contagem