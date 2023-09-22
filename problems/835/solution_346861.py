def melhor_volta(corrida):
    '''Retorna uma tupla com a melhor volta
       da prova, quanto tempo teve e em que
       volta; matriz de 6x10->tuple'''
    tempo=[]
    for desempenho in corrida:
        t=min(desempenho)
        tempo+=[t]
        tf=min(tempo)
        if tf in desempenho:
            corredor=list.index(corrida,desempenho)+1
            volta=list.index(desempenho,tf)+1  
    return corredor, tf, volta