def bolos (A,B,C):
    ''' define a quantidade maxima de bolos que joão pode fazer 
    	int, int,int ---> int '''
    if (A//2) < 1:
        return 0
    elif(B//3) < 1:
        return 0
    elif(C//5) < 1:
        return 0
    elif (A//2) < (B//3) and (A//2) < (C//5):
        return (A//2)
    elif (B//3) < (A//2) and (B//3) < (C//5):
        return (B//3)
    elif (C//5) < (A//2) and (C//5) < (B//3):
        return (C//5)
    else:
        return 0