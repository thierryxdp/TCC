def melhor_volta(A):
	tupla=()
	volta=0
	for i in  range(len(A)):
        for j in range(len(A[i])):
            volta=min(min(elemento) in A)
            tupla=(A[i],volta)
	return tupla