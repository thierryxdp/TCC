def conta_numero(numero,matriz):
    '''função que dado um número inteiro  e uma matriz de inteiros conta e retorna quantas vezes esse numero aparece na matriz
    int,list-> int'''
    proximo=0
    for i in matriz:
        for j in matriz:
            if numero in matriz:
                proximo+=1
    return proximo