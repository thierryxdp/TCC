def melhor_volta(matriz):
    '''funcao que recebe como entrada uma matriz 6x10 cujos elementos sao os tempos em segundos dos corredores em cada volta, e retorna uma tupla informando de quem foi a melhor volta, o tempo da volta e em qual volta o competidor completou o percurso com menor tempo
    list(list) -> tup(int, float, int)'''
    tempos_minimos_competidores=[]
    tempo_minimo=min(linha)
    tempo_minimo_geral=min(tempos_minimos)
    competidor=list.index(tempos_minimos,tempo_minimo_geral)+1
    for linha in matriz:
        list.append(tempos_minimos,tempo_minimo)
        volta=list.index(linha,tempo_minimo)+1
    return (tempo_minimo_geral,competidor,volta)