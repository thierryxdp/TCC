def soma_h(N):
    ''' recebe um numero inteiro e retorna o valor de um numero H com a soma  1 dividido pelos N termos
    da seguinte maneira H= 1 + 1/2 + 1/3...+1/n
    int->boolean'''
    H=0
    for i in range(1,N+1):
        H= H + 1/i
    return round(H,2)