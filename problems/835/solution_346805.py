def melhor_volta(M):
    """função que retorna uma tupla informando quem fez a melhor volta da prova, com qual tempo e em qual volta
    int -> tuple"""
    melhores_temps = []
    voltas = []
    for i in range(len(M)):
        melhor_temp_ind = min(M[i])
        volta = list.index(M[i], melhor_temp_ind) + 1
        voltas.append(volta)
        list.append(melhores_temps, melhor_temp_ind)
    melhor_tempo_geral = min(melhores_temps)
    indice = melhores_temps.index(melhor_tempo_geral)
    competidor = indice + 1
    return (competidor, melhor_tempo_geral, voltas[indice])