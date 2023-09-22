def melhor_volta(matriz):
    '''Recebe uma matriz com os resultados de uma corrida de kart e
    retorna quem teve a melhor volta, o tempo da volta e qual volta foi
    list -> tuple'''
    min=[]
    for linha in matriz:
        min=min+[min(linha)]
        menor_tempo=min(min)
        corredor=list.index(min,menor_tempo)
        return (corredor + 1, menor_tempo, volta + 1)