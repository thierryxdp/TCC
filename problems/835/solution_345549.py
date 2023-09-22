def melhor_volta(m):
    """ a função recebe uma matriz no formato 6x10 (que corresponde aos segundos que cada
    corredor concluiu uma volta) e retorna uma tupla informando de quem foi a melhor
    volta, com qual tempo e em que volta;
    list->tuple"""
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == min m[i][j]:
                tempo = m[i][j]
                corredor = i + 1
                volta = j + 1
    return corredor,tempo,volta