def conta_numero(numero,matriz):
    '''Recebe um numero inteiro e uma matriz de numeros inteiros
    e retorna a quantidade de vezes que aquele numero aparece na matriz;
    int, list -> int'''
    soma=0
    for m in matriz:
        for n in m:
            if n == numero:
                soma+=1
    return soma