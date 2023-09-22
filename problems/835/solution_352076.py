def melhor_volta (matriz: list)-> tuple:
    '''Dada uma matriz 6x10 contendo os tempos em segundos dos competidores
    por volta, retorna uma tupla contendo de quem foi a melhor volta da 
    prova, o tempo dela e em que volta'''
    quem = 0
    t = 99999
    volta = 0
    ind = 1
    for i in matriz:
        if min(i) < t:
            t = min(i)
            quem = ind
            volta = i.index(t) + 1
        ind = ind +1
    return (quem, t, volta)