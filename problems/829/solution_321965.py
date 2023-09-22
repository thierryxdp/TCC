# h = 1 + 1/2 + 1/3 + 1/N
def soma_h(N):
    ''' função que calcula e retorna o valor H com N termos onde N é inteiro e dado como entrada;
    int -> float '''
    x = 0
    for a in range(1, N+1):
          x = x + (1/a)
    return round(x, 2)