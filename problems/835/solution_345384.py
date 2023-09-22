def melhor_volta(voltas):
    menor = []
    for i in range(len(voltas)):
        for j in range(len(voltas[i])):
            menor += [voltas[i],]
    return menor