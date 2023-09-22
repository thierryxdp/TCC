def soma_h(N):
    '''Funcao que dado de entrada um numero inteiro N, retorna
    H, que eh a soma de 1 mais o inverso dos numeros pertencentes
    ao intervalo de 2 até N.
    int -> float'''
    soma = 1
    for numeros in range(2,N+1): # de 2 ate N, por range eh exclui  ultimo
        soma += 1/numeros
    return round(soma,2)