def soma_h(N):
    '''Ao fornecer um numero inteiro, calcula a soma das frações cujo numerador é 1
    e o denominador é cada numero até chegar a N. Ex: soma_h(4): H = 1/1 + 1/2 + 1/3 + 1/4.

    int -> float'''

    H = []
    for numero in range(1,N+1):
        list.append(H,1/numero)

    return sum(H)