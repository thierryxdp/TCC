def melhor_volta(A):
	import math
    min=0
	for i in  range(len(A)):
        for j in range(len(A[i])):
            min=min([(min(elemento),A.index(element),elemento.index(min(element0))) for element0 in A])
	return min