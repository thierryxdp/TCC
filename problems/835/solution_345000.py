def melhor_volta(matriz):
    '''melhor_volta recebe uma matriz 6x10 com os tempos em segundos doscorredores em cada um das dez voltas e devolve uma tuplas com respesctivamente o numero do corredor com a melhor volta da prova, o tempo da melhor volta e em qual volta foi.
    list-->tuple'''
    maisrapido=matriz[0][0]
    voltas=1
    corredor=1
    melhorvolta=[maisrapido]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if maisrapido>=matriz[i][j]:
                maisrapido=matriz[i][j]
                list.append(melhorvolta,matriz[i][j])
                corredor=i+1
                voltas=j+1
    maisrapido=min(melhorvolta)
    
    return (corredor,maisrapido,voltas)