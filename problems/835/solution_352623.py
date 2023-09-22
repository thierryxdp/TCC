def melhor_volta(matriz):
    '''funcao que recebe uma matriz e retorna de quem foi a 
       melhor volta, o seu tempo e em que volta.
       list(list) - > tuple'''
    final = []
    for x in range(len(matriz)):
        list.append(final, min(matriz[x]))
        melhor= list.index(final, min(final))
        tempo= min(final)
        volta= list.index(matriz[melhor], tempo)
    return melhor+1, tempo, volta+1