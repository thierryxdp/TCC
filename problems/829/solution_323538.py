def soma_h(N):
    """dado um numero inteiro N de entrada,
    retorna a soma das frações de 1 sobre denominador
    que se comporta como uma progressão aritmética de termo a1 = 1,
    razão 1 e termo final = N de entrada
    int --> float"""
    termo=1
    for numero in range(2,N+1):
        termo=termo+1/numero
    return round(termo,2)