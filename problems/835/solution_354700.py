def melhor_volta(matriz):
    '''Essa função dada uma matriz contendo o tempo dos corredores em cada volta, 
    retorna uma tupla contendo a informação de quem deu a melhor volta, em qual tempo e em que volta,
    list->tuple'''
    inf_corrida=[]
    for n in matriz:
        melhor_tempo=min(n)
        inf_corrida.append(melhor_tempo)
        tempo=min(inf_corrida)
        piloto=inf_corrida.index(tempo)
        volta=matriz[piloto].index(tempo)
    return (piloto+1,tempo,volta+1)