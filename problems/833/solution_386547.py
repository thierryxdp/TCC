def conta_numero(n,matriz):
    '''funcao que dado um numero inteiro e uma matriz de inteiros de
       tamanho qualquer, conta e retorna quantas vezes aquele numero
       aparece na matriz
       int,list->int'''
    apareceu=0
    for linhas in matriz:
        for colunas in linhas:
            if n==colunas:
                apareceu=apareceu+1
    return apareceu