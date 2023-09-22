def soma_h(N):
    '''funcao que retorna a soma dos inversos de todos os números inteiros positivos menores ou iguais ao numero N de entrada.
    int -> float'''
    H = 0
    for numeros in list(range(1,N+1)):
        H = H + 1/numeros
    return round(H,2)