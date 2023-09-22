def melhor_volta(matriz):
    '''Essa função dada uma matriz contendo o tempo dos corredores em cada volta, 
    retorna uma tupla contendo a informação de quem deu a melhor volta, em qual tempo e em que volta,
    list->tuple'''
    inf_corrida=[]
    for n in matriz:
        inf_corrida.append(min(n))
    return tuple(inf_corrida)