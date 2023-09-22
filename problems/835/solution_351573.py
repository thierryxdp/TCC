def melhor_volta(matriz):
    
    tempos = []
    for i in range(len(matriz)):
        for e in matriz [i]:
            tempos += [e]
    menor_tempo = min(tempos)
    corredor = tempos.index(menor_tempo)//10
    volta = tempos.index(menor_tempo)%10
    return (corredor+1,menor_tempo,volta+1)