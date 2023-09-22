def melhor_volta(matriz):
    '''Função que recebe um matriz de 6 corredores e 10 voltas e retorna 
    uma tupla contendo o corredor que fez melhor volta, o tempo que feze em que volta
    list(list)-> tuple'''
    menor_tempo=0
    for volta in range(0, len(matriz)):
        for tempo in range(0, len(matriz[volta])):
            if  min(matriz[volta][tempo], menor_tempo)== matriz[volta][tempo]:
                tmp = min((matriz[volta][tempo], menor_tempo))
                index = list1.index(tmp)
                campeao=volta+1
                volta=tempo+1
                return(campeao, tmp, volta)