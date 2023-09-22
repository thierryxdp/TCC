def soma_h(n):
    '''retorna a soma dos inversos dos naturais ate um numero n; int -> float'''
    i = 1
    inversos = []
    while i <= n:
        inversos = inversos +[1/i,]
        i = i + 1
    return round(sum(inversos),2)