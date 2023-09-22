def melhor_volta(lista):
    l = []
    for x in lista:
        for y in range(len(x)):
            l.append(x[y])
            menor_tempo = min(l)
            z = lista[y].index(menor_tempo)
    return z, menor_tempo