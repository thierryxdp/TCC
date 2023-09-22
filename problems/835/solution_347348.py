def melhor_volta(matriz):
    corredor=1
    volta=1
    melhorVolta=matriz[0][0]
    resultado=(corredor,melhorVolta,volta)
    for linhas in range(len(matriz)):
        menosTempoCorredor=min(matriz[linhas])
        melhorTempo=min(melhorVolta,menosTempoCorredor)
        for colunas in range(len(matriz[0])):
            tempo=matriz[linhas][colunas]
            if tempo==melhorVolta:
                resultado=linhas+1,melhorVolta,colunas+1
                    
    return resultado