def melhor_volta(M):
    """Funcao que retorna quem foi o corredor com melhor tempo de prova, com que tempo e em que volta.
    List(list) - > tuple"""
    lista_tempos= []
    for i in range(6):
        list.append(lista_tempos,min(M[i]))
    melhor_tempo = min(lista_tempos)
    corredor = lista_tempos.index(melhor_tempo)+1
    volta = M[corredor-1].index(melhor_tempo)+1
    return (corredor, melhor_tempo, volta)