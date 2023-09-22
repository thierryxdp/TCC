def conta_numero(num, mat):
    x = 0
    if num in mat:
        for i in range(mat):
            for j in mat[i]:
                if j == num:
                    x += 1
    return x