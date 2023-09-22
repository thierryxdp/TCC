def melhor_volta(A):
    min_volta=0
    for i in  range(len(A)):
        for j in range(len(A[i])):
             if current_volta < min_volta:
            	min_volta=min(A[i][j])
    return min_volta