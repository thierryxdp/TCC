def soma_h(N):
    '''Função que retorna a soma dos inversos dos números 
    do um intervalo de 1 até o valor N inserido
    int -> float'''
    soma = 0
    for valor in range(1, N+1):
        soma = soma + 1/valor
    return round(soma, 2)