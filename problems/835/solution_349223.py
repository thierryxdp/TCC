def melhor_volta(M):
    '''Função que receba uma matriz com os tempos em segundos dos corredores em cada volta, e que deve retornar quem foi a melhor volta da prova, o tempoe e a volta.
List -> Tuple'''
    T = [] # menores tempos de cada um
    V = [] # nmr da volta de melhor tempo de cada um
    for corredor in M:
        T.append(min(corredor))
        V.append(list.index(M, corredor))
        melhor_tempo= min(T)
        de_quem = list.index(T, melhor_tempo)
        qual_volta= list.index(M[de_quem], melhor_tempo)
    return ((de_quem + 1),(melhor_tempo),(qual_volta + 1))