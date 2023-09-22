def melhor_volta(M):
    '''Função que dada uma matriz 6x10 com tempos de volta de corredores,
    retorna quem fez a melhor volta, com qual tempo e em que volta
    list -> tuple'''
    dados = ()
    corredor = 0
    volta = 0
    for i in range(len(M)):
        if i == 0:
            menor_tempo = min(M[i])
        elif menor_tempo > min(M[i]):		
        	menor_tempo = min(M[i])
            corredor = i + 1
            volta = list.index(M[i], menor_tempo) + 1
    return (corredor, menor_tempo, volta)