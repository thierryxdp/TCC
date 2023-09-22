def conta_numero(a,lis):
    con=0
    for i in range(len(lis)):
        for j in range(len(lis[i])):
            if(lis[i][j]==a):
                con=con+1
	return con