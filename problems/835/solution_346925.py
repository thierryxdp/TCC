def melhor_volta(matriz):
    ''' Recebe como entrada uma matriz 6 x 10 com os tempos em segundos dos corredores em cada volta. A função
    retorna uma tupla informando: De quem foi a melhor volta da prova, com qual tempo e em que volta. '''
    tempos=[]

    for corredor in matriz:
        tempos.append(min(corredor))
        if min(tempos) in corredor:
            top1 = matriz.index(corredor)
            volta = corredor.index(min(tempos))

    return (top1+1,min(tempos),volta+1)