def conta_numero(numero,matriz):
    '''funcao que recebe um numero inteiro e uma matriz e retorna a quantidade de vezes
    que o numero aparece na matriz
    int,list->int'''
    contagem=0
    for elementos in matriz[0]:
    	if (elementos==numero):
            contagem+=1
    return contagem