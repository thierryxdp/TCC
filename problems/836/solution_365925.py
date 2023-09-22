def busca(setor,matriz):
    if matriz==[]:
        return 0
    else:
        linhas=len(matriz)
        colunas=len(matriz[0])
        ocorr=[]
        for i in range(linhas):
            ocorrencia = 0
            for j in range(colunas):
                if matriz[i][j] == setor:
                    ocorrencia = ocorrencia + 1
            ocorr=ocorr+[matriz[i][j]]
        return ocorr