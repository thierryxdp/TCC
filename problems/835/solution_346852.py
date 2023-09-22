def melhor_volta(corrida):
    '''Retorna uma tupla com a melhor volta
       da prova, quanto tempo teve e em que
       volta; matriz de 6x10->tuple'''
    tempo=[]
    melhorVolta=corrida[0][0]
    for desempenho in corrida:
        t=min(desempenho)
        tempo+=[t]
        if t<melhorVolta:
            tf=min(tempo)
            corredor=list.index(corrida,desempenho)+1
            volta=list.index(desempenho,tf)+1     
    return corredor, tf, volta