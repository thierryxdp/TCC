def melhor_volta(corrida):
    '''Retorna uma tupla com a melhor volta
       da prova, quanto tempo teve e em que
       volta; matriz de 6x10->tuple'''
    for e in corrida:
        t=min(corrida)
        tempo=min(t)
        corredor=list.index(corrida,t)+1
        volta=list.index(t,tempo)+1
    return corredor, tempo, volta