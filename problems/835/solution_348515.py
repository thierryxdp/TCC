def melhor_volta(lista):
    x=0
    volta=0
    corredor=()
    while x < len(lista):
        corredor =corredor,min(lista[x])
        x=x+1
    return corredor.split(,)