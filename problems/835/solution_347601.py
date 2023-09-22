def melhor_volta(matriz):
    '''dada uma matriz 6x10 com os tempos em segundos dos corredores em cada volta,
    retorna uma tupla contento, respectivamente, quem fez a melhor volta da prova,
    com qual tempo e em que volta;
    list --> tupla'''
    melhores_voltas = []
    quais_voltas = []
    for linha in matriz:
        melhor_cada_corredor = min(linha)
        qual_volta = list.index(linha, melhor_cada_corredor)
        list.append(melhores_voltas, melhor_cada_corredor)
        list.append(quais_voltas, qual_volta)
    melhor_geral = min(melhores_voltas)
    qual_corredor = list.index(melhores_voltas, melhor_geral)
    qual_volta2 = quais_voltas[qual_corredor]
    return (qual_corredor+1,melhor_geral,qual_volta2+1)