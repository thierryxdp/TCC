def melhor_volta(matriz):
    '''funcao que recebe uma matriz 6 x 10 com os tempos
    em segundo dos corredores em cada volta, retornando uma
    tupla indicando quem foi a melhor volta da prova,com qual tempo
    e em que volta
    list->tuple'''
    tupla_vazia=()
    cada_tempo=[]
    for linhas in matriz:
        for colunas in linhas:
            list.append(cada_tempo,colunas)