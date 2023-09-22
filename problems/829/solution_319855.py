def soma_h(n):
    ''' essa função rece um numero inteiro e retorna o valor H da soma harmonica
    int -> float'''
    soma = 0
    for x in range(1, n+1):
        soma += 1/x
    return round(soma, 2)