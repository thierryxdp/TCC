def melhor_volta(matriz):
    '''Recebe uma matriz com os resultados de uma corrida de kart e
    retorna quem teve a melhor volta, o tempo da volta e qual volta foi
    list -> tuple'''
    minimo=[]
    for linha in matriz:
        minimo=minimo+[min(linha)]
        menor_tempo=min(minimo)
        corredor=list.index(minimo,menor_tempo)
        return (corredor + 1, menor_tempo, volta + 1)