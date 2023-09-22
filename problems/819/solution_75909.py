def multiplos(lista,numero):
    i = 0
    multiplos = []
    while i < len(lista):
        if lista[i] % numero == 0:
            multiplos.append(lista[i])
        i = i + 1
    return multiplos