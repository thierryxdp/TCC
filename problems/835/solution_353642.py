def melhor_volta(matriz):
    '''Retorna uma tupla informando quem foi o vencedor da prova.
    list-->tuple'''
    melhor_tempo=matriz[0][0]
    lista=[]
    
    for linha in range(len(matriz)):  
        melhor_tempo=min(linha)
        if melhor_tempo(linha) < melhor_tempo:
            return melhor_tempo==melhor_tempo(linha)