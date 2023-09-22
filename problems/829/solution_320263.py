def soma_h(N):
    '''Dado N termos, calcule o valor da função H; int -> float'''
    soma=1
    div=1
    for x in range(2,N+1):
        soma=soma+1/x
    return round(soma,2)