def conta_numero(numero, matriz):
    ''' funcao que dada um numero inteiro e uma matriz independente de tamanho retorna o numero de vezes que o numero apareceu na matriz
    int, int-> int'''
    count = 0
    for i in matriz:
        for n in i:
            if n==numero:
                count+=1
    return(count)