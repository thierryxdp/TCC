def bolos(A, B, C):
    farinha = A//2
    ovos = B//3
    leite = C//5
    limite = farinha
    if ovos < limite and leite >= limite:
        limite = ovos
    elif leite < limite:
        limite = leite
    return limite