def melhor_volta(matriz):
    '''Dada uma matriz 6x10, na qual as linhas representam
    os tempos de cada piloto e as colunas são os tempos em si,
    retorna uma tupla informando de quem foi a melhor volta,
    com qual tempo e em que volta; list[list[int]] -> tuple[int]'''
    lfinal = []
    i=0
    for linha in matriz:
        j=0
        tempomelhorvolta = min(matriz[i])
        if tempomelhorvolta in matriz[i]:
            pilotomelhorvolta = matriz[i].index(min(matriz[i]))
        for coluna in matriz[i]:
            qualmelhorvolta = matriz[i].index(tempomelhorvolta)
            j+=1
        i+=1
    final.append(pilotomelhorvolta)
    final.append(tempomelhorvolta)
    final.append(qualmelhorvolta)
    return tuple(final)