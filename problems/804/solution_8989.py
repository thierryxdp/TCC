def filtra_pares(tupla):
    
    pares=[]
    for i in range(tupla):
        for j in range(tupla[i]):
        	if tupla[i][j]%2==0:
            	pares.append(tupla[i])
    return pares