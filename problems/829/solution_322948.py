def soma_h(N):
    '''Funçao que calcula e retorna o valor H com N termos, retornando seu resultado com duas casas decimais.int->int'''
    soma = 1
    for i in range(1,N):
        if N>= 1:
            soma = soma + 1/N
            N = N - 1
        i = i + 1
    return round(soma,2)