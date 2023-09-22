def conta_numero(numero,matriz):
    ''' dado um numero inteiro e uma matriz de inteiros de
    tamanho qualquer, conta e retorna quantas vezes aquele
    numero aparece na matriz;
    entrada:int,list
    saida:int'''
    count=0
    for i in matriz:
        for j in i:
            if j == numero:
                count= count+1
    return count