def melhor_volta(matriz):
    '''funcao que recebe uma matriz 6 x 10 com os tempos
    em segundo dos corredores em cada volta, retornando uma
    tupla indicando de quem foi a melhor volta da prova,com qual tempo
    e em que volta
    list->tuple'''
    tupla_vazia=()
    menor_tempo_dos_jogadores=[]
    em_qual_volta=1
    for linhas in matriz:
        for volta in linhas:
            list.append(menor_tempo_dos_jogadores,min(linhas))
    menor_tempo=min(menor_tempo_dos_jogadores)
    for linhas1 in matriz:
        for volta1 in linhas:
            if volta1==menor_tempo:
                em_qual_volta= em_qual_volta + list.index(matriz,min(linhas1))
                return (list.index(matriz,linhas1),menor_tempo,em_qual_volta)