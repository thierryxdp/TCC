def busca(setor,matriz):
    if matriz==[]:
        return 0
    else:
        linhas=len(matriz)
        colunas=len(matriz[0])
        ocorr=[]
        for i in range(linhas):
        	if matriz[i][2]==setor:
        		matriz[i].remove(setor)
        		ocorr=ocorr+[matriz[i][j]]
        return ocorr