def soma_h(n):
    '''Calcula e retorna o valor H com N termos onde N é inteiro e dado como entrada:
h = 1+1/2+1/3+1/N
int -> float'''
    x = 0
    for i in range(1, n+1):
          x = x + (1/ i)
    return round(x,2)