def conta_numero(numero,matriz):
    '''função que dado um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele número aaprece na matriz; int, list (mat) -> int'''
    total=0
    for i in matriz:
        for j in i:
            if numero==j:
                total+=1
    return total