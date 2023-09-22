def melhor_volta(lista):
    l = []
    for x in lista:
        for y in range(len(x)):
            l.append(x[y])
            menor_tempo = min(l)
            a = x.index(menor_tempo)
            
    return menor_tempo, a