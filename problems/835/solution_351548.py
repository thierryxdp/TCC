def melhor_volta(m):
    '''Recebe uma matriz contendo tempo em segundo dos corredores em cada volta e retorna uma tupla com o número do corredor que obteve a melhor volta, o tempo da volta e o nnúmero da volta; list->tuple'''
    mintempo=min(min(m[0]),min(m[1]),min(m[2]),min(m[3]),min(m[4]),min(m[5]))                                                  
    for corredor in m:
        for volta in m:
            if volta==mintempo:
                vencedor=list.index(m,corredor)+1
                numvolta=list.index(corredor,volta)+1
    return (vencedor,mintempo,volta)