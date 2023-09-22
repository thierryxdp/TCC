def melhor_volta(corrida):
    '''
    Recebe uma matriz corrida onde cada entrada contém o tempo de um corredor em umas volta
    e retorna uma tupla com o número do melhor corredor, o seu tempo, e o número da volta
    
    list -> (int, float, int)
    '''
    melhor=(1,corrida[0][0],1)
    i=0
    while i<len(corrida):
        j=0
        while j<len(corrida[i]):
            if corrida[i][j]<melhor[1]:
                melhor=(i+1,corrida[i][j],j+1)
            j+=1
        i+=1
    return melhor