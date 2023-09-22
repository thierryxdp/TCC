def conta_numero(num,mat):
    total=0
    for i in mat:
            if num in mat[i]:
                total=total+1
            else:
                total=total
    return total