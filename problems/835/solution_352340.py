def melhor_volta(A):
	import math
    min=0
	for i in  range(len(A)):
        for j in range(len(A[i])):
            min=min([(min(A[i][j]),A.index(A[i][j])
     return min