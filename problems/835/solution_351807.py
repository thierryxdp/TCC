def melhor_volta(matriz):
    '''
        Dada uma matriz com as 10 voltas de 6 corredores, retorna qual a melhor volta
        dizendo o corredor, o tempo feito e em qual volta
    '''
    melhores_tempos=[]
    corredor=0
    for i in matriz:
        melhores_tempos.append(min(i))
    for j in melhores_tempos:
        corredor=list.index(melhores_tempos,min(melhores_tempos))
    tempo=min(melhores_tempos)
    volta= list.index(matriz[corredor],tempo)+1
    return (corredor+1,tempo,volta)