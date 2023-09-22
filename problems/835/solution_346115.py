def melhor_volta(matriz):
    '''informa de quem dos 6 corredores foi a melhor volta, o tempo e qual das 10 voltas foi a meis veloz
    lista->tupla'''
    piloto=0
    melhor=999999999999
    for corredor in matriz:
        piloto+=1
        volta=0
        for tempo in corredor:
            volta+=1
            if tempo<melhor:
                melhor=tempo
                qual=volta
                quem=piloto
    
    return(quem,melhor,qual)