def filtraMultiplos(listanum,n):
    listnum = []
    i = 0
    while i < len(listanum):
        if listanum [i]%n == 0:
			listnum.append(listnum[i])
    	i = i+1
	return listnum