def melhor_volta(voltas):
    ''' funcao que dada uma matriz 6x10 com as 10 voltas dos 6 corredores ela retorne uma tupla dizendo de quem foi a melhor volta ,o menor tempo e em que volta ocorreu
    list->tuple'''
    tempo=[]
    for i in range(len(voltas)):
        tempo= tempo+[min(voltas[i])]
    menortempo=min(tempo)
    piloto= list.index(tempo,menortempo)
    piloto+=1
    volta =list.index(voltas[piloto],menortempo)
    volta+=1
    return (piloto,menortempo,volta)