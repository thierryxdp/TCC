def colisao(x,y):
	x = [2][2]
    y = [2][2]
	#scanf("%d %d %d %d",&x[0][0],&y[0][0],&x[0][1],&y[0][1]);
    #scanf("%d %d %d %d",&x[1][0],&y[1][0],&x[1][1],&y[1][1]);
    if (x[0][1] < x[1][0] or x[1][1] < x[0][0] or y[0][1] < y[1][0] or y[1][1] < y[0][0] or x[0][0] > x[1][1] or x[1][0] > x[0][1] or y[0][0] > y[1][1] or y[1][0] > y[0][1]):
    	return(True)
    else:
    	return(False)