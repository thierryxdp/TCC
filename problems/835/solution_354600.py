def melhor_volta(M):
    dados=()
    menor_tempo=0
    for i in range(len(M)):
        if menor_tempo > min(M[i]):		
        	menor_tempo = min(M[i])
            corredor = i
            volta = list.index(M[i], menor_tempo)
    return (corredor, menor_tempo, volta)