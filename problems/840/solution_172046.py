def bolos(farinha,ovos,leite):
    farinha=Math.floor(farinha/2)
    ovos = Math.floor(ovos/3)
    leite = Math.floor(leite/5)
    minimo = farinha
    if (ovos<minimo):
        minimo=ovos
        return minimo
    elif (leite<minimo):
        minimo=leite
        return minimo
    else:
        return minimo