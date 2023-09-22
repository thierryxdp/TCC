def soma_h(n):
    '''Função que calcula e retorna o valor H com N termos
int -> float'''
    H=0

    for i in range(1,n+1):
        H += 1.0/i

    return round(H,2)