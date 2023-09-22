def melhor_volta(matriz):
    '''Dada uma matriz 6x10 com tempos
       de corredores em cada volta. A 
       funcao retorna de quem foi a melhor
       volta, com qual tempo e em que volta;
       list -> int, int, int'''
    i = 0 
    while i < len(matriz):
        for elemento in matriz[i]:
            menor_tempo=0
            if elemento < 100:
                menor_tempo=elemento
            if elemento < menor_tempo:
                menor_tempo=elemento
        i = i+1            
    return (i+1,elemento,menor_tempo)