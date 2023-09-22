def_numero(a,lis):
    con=0
    for i in len(lis):
        for j in len(lis[i]):
            if(lis[i][j]==a):
                con=con+1
	return con