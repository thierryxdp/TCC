def melhor_volta(lista):
    soma = 0
    for x in lista:
        for y in x:
            tempo = min(x)
            v = x.index(tempo)
    return tempo, v