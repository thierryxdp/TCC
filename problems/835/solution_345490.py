def melhor_volta(matriz):
    """Retorna uma tupla informando de quem foi a melhor volta, com qual tempo e em que volta; list -> tuple."""
    x= []
    z = []
    for i in range(0, 5):
        list.append(x, min(matriz[i]))
        list.append(z, list.index(matriz, min(matriz[i])))
    return ((list.index(x, min(x)) + 1), min(x), list.index(z, (list.index(x, min(x))))