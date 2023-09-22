def melhor_volta(matriz):
    '''Recebe uma matriz que representa o tempo da volta de 6 corredores em 10 voltas diferentes e retorna qual corredor teve o menor tempo, o menor tempo e em qual volta
    list(list)->tuple'''
    menores_tempos=[]
    for i in matriz:
        menores_tempo= menores_tempo + [min(i)]
    menor_tempo_total= min(menores_tempo)
    corredor=list.index(menores_tempos,menor_tempo_total)
    volta= list.index(menores_tempos[corredor],menor_tempo_total)
    return (corredor,menor_tempo_total,volta)