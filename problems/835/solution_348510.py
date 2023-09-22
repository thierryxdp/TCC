def melhor_volta(lista):
    x=0
    volta=min(lista[x])
    corredor=0
    while x < len(lista):
        volta = volta,min(lista[x])
        x=x+1
    return volta