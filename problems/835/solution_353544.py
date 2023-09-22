def melhor_volta (matriz):
    '''função que dada a uma matriz com os tempos de cada corredor
    de kart, retorna quem teve a melhor volta, com qual tempo
    e em que volta, respectivamente.
    list -> tuple'''
    
    corredor = 1
    melhor_tempo = 1
    ind = 1
    volta = 1
    
    
    for i in range(len(matriz)):
        if matriz [i] == min (matriz):
            corredor += len (matriz[:i+1])
            melhor_tempo += min (matriz[i])    
        for j in matriz [i]:
            if matriz [i] == min (matriz):
                if j == ind:
                    return (corredor,melhor_tempo,volta)
                ind += 1