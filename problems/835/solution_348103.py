def melhor_volta(tempos):
    acumulador=[]
    menortempo=min(tempos)
    volta=0
    corredor=0
    for corredores in range(len(tempos)):
        for tempoporvolta in range(len(tempos[0])):
            if tempos[corredores][tempoporvolta]<min(tempos):
                min(tempos)=tempos[corredores][tempoporvolta]
                volta=tempoporvolta+1
                corredor=corredores+1
    return corredor,min(tempos),volta