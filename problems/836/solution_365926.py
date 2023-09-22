def busca(setor,matriz):
    if matriz==[]:
        return 0
    else:
        linhas=len(matriz)
        colunas=len(matriz[0])
        ocorr=[]
        for i in range(linhas):
            if matriz[i][2] == setor:
            ocorrencia=[]
            for j in range(colunas):
            		if matriz[i][j]!=setor:
            			ocorrencia+=matria[i][j]
            ocorr+=[ocorrencia]
        return ocorr