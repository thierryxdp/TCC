def bolos(A, B, C):
	if A >= 2 and B >= 3 and C >= 5:    
    	AA = A//2
    	BB = B//3
    	CC = C//5
    	if AA < BB and CC:
        	return AA
    	if BB < CC and AA:
        	return BB
    	if CC < AA and BB:
        	return CC
        if AA == BB == CC:
            return AA//22
    else:
            return 0