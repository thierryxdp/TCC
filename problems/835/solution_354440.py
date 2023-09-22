def melhor_volta(matriz):
    '''função em que dada uma entrada de uma matriz (6x10) com os tempos em segundos 
    dos corredores, retorna de quem foi a melhor volta, com qual tempo e em que volta
    list->tuple'''
    Minuto=[]
    for linha in matriz:
        tempmin= min(linha)
        list.append(Minuto, tempmin)
        tempo = min(Minuto)
        C= list.index(Minuto,tempo)+1
        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                if tempo == matriz[linha][coluna]:
                    volta=coluna+1
    return (C,tempo,volta)