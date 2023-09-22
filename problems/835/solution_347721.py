def melhor_volta(matriz):
    '''Dada uma matriz 6x10 com tempos
       de corredores em cada volta. A 
       funcao retorna de quem foi a melhor
       volta, com qual tempo e em que volta;
       list -> int, int, int'''
    i = 0 
    j = 0
    d = 0
    menor_tempo=100
    menorestempo=[]
    while i < len(matriz):
        for elemento in matriz[i]:
            if elemento < menor_tempo:
                menor_tempo=elemento
                menorestempo = [menor_tempo] + menorestempo
        i = i+1 
    while j < len(matriz):
        matriz2 = matriz[j]
        for elem in matriz2:
            if elem == min(menorestempo):
                return (j,min(menorestempo))      
        j = j + 1