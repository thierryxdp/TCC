def melhor_volta(matriz):
    """
    Dada uma matriz com o tempo de cada uma das 10 voltas (10 colunas)
    de cada um dos 6 corredores (6 linhas), retorna-se de qual corredor
    foi a melhor volta (de 1 a 6), qual foi o tempo que ele percorreu e
    qual foi a volta (de 1 a 10).
    Entrada: matriz -> list(lists)
    Retorna: tupla
    """
    melhores_tempos = []
    
    for i in range(0,6):
        tempos_indiv = matriz[i][:]
        tempos_indiv_ordem = matriz[i][:]
        list.sort(tempos_indiv_ordem)
        melhores_tempos += tempos_indiv_ordem[5]
    
    melhor_tempo = melhores_tempos[:]
    list.sort(melhor_tempo)

    melhor_corredor = list.index(tempos_indiv,tempos_indiv_ordem(5)) + 1
    melhor_volta = list.index(matriz[melhor_corredor-1],list.index(melhores_tempos,melhor_tempo[9])) + 1
    
    return (melhor_corredor,melhor_tempo[9],melhor_volta)