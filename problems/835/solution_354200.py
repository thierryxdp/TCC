def melhor_volta(tempos):
    '''função que recebe uma matriz com os tempos dos 6 corredores em 10 voltas e retorna o corredor com a melhor volta
       list -> tuple'''
    menores_tempos=[]
    melhores_voltas=[]
    i=0
    while i<len(tempos):
        menor_tempo= min(tempos[i])
        melhor_volta= list.index(melhores_voltas, menor_tempo)
        list.append(melhores_voltas, melhor_volta)
        list.append(menores_tempos, menor_tempo)
        i=i+1
    melhor_corredor=list.index(menores_tempos, min(menores_tempos))+1
    melhor_volta_total= melhores_voltas[melhor_corredor-1]
    return (melhor_corredor, min(menores_tempos), melhor_volta_total)