def soma_h(n):
    '''Função que dado um numero n inteiro, retorne
    valor H com 2 casas decimais
    entrada: int
    saída: float'''
    H = 0
    for numero in range(1,n+1):
        H += 1/numero
    return round(H,2)