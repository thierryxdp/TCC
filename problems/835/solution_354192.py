def melhor_volta(tempos):
    '''função que recebe uma matriz com os tempos dos 6 corredores em 10 voltas e retorna o corredor com a melhor volta
       list -> tuple'''
    menores_tempos=[]
    for linha in tempos:
        menor_tempo=min(linha)
        list.append(menores_tempos, menor_tempo)
    melhor_corredor=list.index(menores_tempos,min(menores_tempos)) + 1
    return (melhor_corredor, min(melhores_tempos))