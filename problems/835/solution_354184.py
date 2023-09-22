def melhor_volta(matriz):
	linhas= len(matriz)
    colunas= len(matriz[0])
    tempos=()
	for i in range (linhas):
	    for j in range (colunas):
            tempos=(matriz[i][j],) + tempos
        	menor=min(tempos)
            piloto=list.index(tempos,menor)
    return (piloto,menor,colunas)