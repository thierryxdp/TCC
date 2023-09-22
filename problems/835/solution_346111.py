def melhor_volta(r):
    '''Dado uma matriz com o tempo dos corredores, retorna
    uma tupla comquem foi a melhor volta da prova, o melhor tempo e
    em qual volta.
    list --> tuple'''
    melhorvolta = []
    
    for corredor in r:
        list.append(melhorvolta,min(corredor))
        
    a = min(melhorvolta)
    b = list.index(melhorvolta,a)
    c = list.index(r[b],a)
    
    return (b+1,a,c+1)