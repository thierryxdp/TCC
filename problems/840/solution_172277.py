def bolos(x, y, z):
    farinha = x // 2
    ovos = y // 3
    leite = z // 5
    bolo = (farinha >= 2), (ovos >= 3), (leite >= 5)
    return bolo