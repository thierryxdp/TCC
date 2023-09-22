def soma_h(numero):
    '''dado um numero inteiro N(numero), calcula H(H=1+1/2+1/3+1/4+...+1/N) em funcao de N;
    retorna o valor H com aproximacao de 2 casas decimais; int -> float'''
    H = 0
    for numeroX in range(1,numero+1):
        H += 1/numeroX
    return round(H, 2)