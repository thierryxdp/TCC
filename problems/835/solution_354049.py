def melhor_volta(m):
    '''
    	funcao que dada uma matriz 6x10 com os tempos dos corredores 
        em cada volta, retorna o numero do melhor corredor, seu melhor
        tempo e em qual volta esse tempo foi feito.
        list -> tuple
    '''
    melhor_tempo = []
    melhor_volta_corredor = []
    for i in m:
        t = min(i)
        list.append(melhor_tempo, t)
        v = list.index(i, min(i))
        list.append(melhor_volta_corredor, v)
        
    x = list.index(melhor_tempo, min(melhor_tempo))
    y = min(melhor_tempo)
    z = melhor_volta_corredor[x]
    return (x+1, y, z+1)