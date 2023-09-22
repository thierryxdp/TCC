def melhor_volta(M):
    dados=()
    corredor=0
    volta=0
    for i in range(len(M)):
        if i == 0:
            menor_tempo =min(M[i])
        elif menor_tempo > min(M[i]):		
        	menor_tempo = min(M[i])
            corredor = i + 1
            volta = list.index(M[i], menor_tempo) + 1
    return (corredor, menor_tempo, volta)