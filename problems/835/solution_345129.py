def melhor_volta(matriz):
    '''recebe uma matriz com o tempo das 10 voltas dos 6 corredores, e retorna uma tupla
    contendo qual corredor fez a melhor volta, o tempo dela e qual foi o numero da volta
    list-->tuple'''
    minimos=[]
    volta=[]
    for i in matriz:
        melhor_volta=min(i)
        list.append(minimos,melhor_volta)
        list.append(volta,list.index(i,melhor_volta)+1)
    melhor=min(minimos)
    index_melhor=list.index(minimos,melhor)
    return (index_melhor+1,melhor,volta[index_melhor])