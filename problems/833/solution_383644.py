def conta_numero(numero,matriz):
    '''Dado um numero inteiro e uma matriz de 
       inteiros a funcao retorna quantas vezes
       o numero aparece na matriz;
       int , list -> int'''
    i = 0
    contagem = 0
    while i < len(matriz):
        for elemento in matriz[i]:
            if elemento == numero:
                contagem = 1 + contagem 
        i = i + 1
    return contagem