def melhor_volta(m):
    '''Função que dada uma matriz m com os tempos em segundo em cada volta de cada corredor, retorna uma tupla informando de quem foi a melhor volta, com qual tempo e em que volta
    list[list] -> tuple(int, float, int)'''
    corredor=0
    tempo=0
    volta=0
    for i in range(len(m)):
        if min(m)==m[i]:
            corredor=list.index(m,m[i])+1
        for j in range(len(m[0])):
            if min(min(m))==m[i][j]:
                tempo=m[i][j]
                volta=list.index(m[i],m[i][j])+1
    resultado=corredor,tempo,volta
    return resultado