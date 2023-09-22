def melhor_volta(lista):
    soma = 0
    l = []
    for x in lista:
        for y in range(len(lista)+1):
            l.append(x[y])
    tempo = min(l)
    return tempo