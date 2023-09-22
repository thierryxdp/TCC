def multiplos(lista,numero):
    i = 0
    multiplos = []
    while i < len(lista):
        if lista[i] % numero == 0:
            multiplos.append(lista[i])
        i = i + 1
    return multiplos
print(multiplos((1,2,3,4,5,6,7,8,9,10,11,12),3))