def melhor_volta(m):
    '''Função que dada uma matriz m com os tempos em segundo em cada volta de cada corredor, retorna uma tupla informando de quem foi a melhor volta, com qual tempo e em que volta
    list[list] -> tuple(int, float, int)'''
    corredor=0
    tempo=0
    volta=0
    for i in m:
        if min(m)==i:
            corredor=list.index(m,i)+1
        for j in i:
            if min(min(m))==j:
                tempo=j
                volta=list.index(i,j)+1
    resultado=corredor,tempo,volta
    return resultado