def melhor_volta(A):
	min=0
	for i in  range(len(A)):
        for j in range(len(A[i])):
            min=min([(min(element),mat.index(element),element.index(min(element))) for element in mat])
	return min