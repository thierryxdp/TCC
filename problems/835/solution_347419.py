def melhor_volta(matriz):
    '''Funçao que recebe uma matriz com os 10 temposde 6 corredores de
    kart diferentes e busca o menor tempo deles. Retorna uma tupla 
    informando qual foi o jogador, qual o tempo e em que volta foi
    list -> tuple'''
    tempos=[]
    voltas=[]
    for i in range(len(matriz)):
        menor= min(matriz[i])
        list.append(tempos,menor)
        list.append(voltas, list.index(matriz[i],menor))
    tempo= min(tempos)
    corredor= list.index(tempos,tempo)
    volta= voltas[corredor]
    return (corredor+1, tempo, volta+1)