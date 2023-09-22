def soma_h(N):
    '''Função calcula e retorna a soma dos inversos de 1 a n;
    int -> float'''

    lista_H = list(range(1,N+1))
    H = 0
    for i in lista_H:
        i = i**-1
        H += i
    return round(H,2)