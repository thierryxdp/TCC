def melhor_volta(tempos):
    '''função que recebe uma matriz com os tempos dos 6 corredores em 10 voltas e retorna o corredor com a melhor volta
       list -> tuple'''
    menores_tempos=[]
    melhor_volta=[]
    for linha in tempos:
        menor_tempo=min(linha)
        volta= list.index(linha,menor_tempo)+1
        list.append(menores_tempos, menor_tempo)
    melhor_corredor=list.index(menores_tempos,min(menores_tempos)) + 1
    volta=list.index(linha, menor_tempo)+1
    return (melhor_corredor, min(menores_tempos, volta))