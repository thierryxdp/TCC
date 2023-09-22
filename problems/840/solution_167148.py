def bolos(A,B,C):
	if(A//2 == 0 or B//3 == 0 or C//5 == 0):
		return 0
	else:
		return max(A//2,B//3,C//5)