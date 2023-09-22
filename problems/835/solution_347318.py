def melhor_volta(corrida):
    '''função que recebe uma matriz com os tempos de cada volta de
    cada corredor em uma pista de kart e retorna uma tupla informando
    de quem foi a melhor volta, com qual tempo e qual volta.'''
    minimo1 = min(corrida[0])
    minimo2 = min(corrida[1])
    minimo3 = min(corrida[2])
    minimo4 = min(corrida[3])
    minimo5 = min(corrida[4])
    minimo6 = min(corrida[5])
    resultado = ()
    if minimo1 < minimo2 and minimo1 < minimo3 and minimo1 < minimo4 and minimo1 < minimo5 and minimo1 < minimo6:
        resultado = resultado + (1, minimo1, (corrida[0].index(minimo1))+1)
    elif minimo2 < minimo1 and minimo2 < minimo3 and minimo2 < minimo4 and minimo2 < minimo5 and minimo2 < minimo6:
        resultado = resultado + (2, minimo2)
    elif minimo3 < minimo2 and minimo3 < minimo1 and minimo3 < minimo4 and minimo3 < minimo5 and minimo3 < minimo6:
        resultado = resultado + (3, minimo3)
    elif minimo4 < minimo2 and minimo4 < minimo3 and minimo4 < minimo1 and minimo4 < minimo5 and minimo4 < minimo6:
        resultado = resultado + (4, minimo4)
    elif minimo5 < minimo2 and minimo5 < minimo3 and minimo5 < minimo4 and minimo5 < minimo1 and minimo5 < minimo6:
        resultado = resultado + (5, minimo5)
    else:
        resultado = resultado + (6, minimo6)