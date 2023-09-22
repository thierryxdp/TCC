def melhor_volta(matriz):
    melhorVolta=matriz[0][0]
    resultado=(1,melhorVolta,1)
    for linhas in range(len(matriz)):
        menosTempoCorredor=min(matriz[linhas])
        melhorVolta=min(melhorVolta,menosTempoCorredor)
        for colunas in range(len(matriz[0])):
            tempo=matriz[linhas][colunas]
            if tempo==melhorVolta:
                resultado=linhas+1,melhorVolta,colunas+1
                    
    return resultado