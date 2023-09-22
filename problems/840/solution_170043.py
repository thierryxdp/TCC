def bolos(A, B, C):
    farinha = A//2
    ovos = B//3
    leite = C//5
    limite = farinha
    if ovos < limite and farinha >= limite:
        limite = ovos
    elif leite < limite and ovos >= limite:
        limite = leite
    return limite