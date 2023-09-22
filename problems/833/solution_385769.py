def conta_numero(num, mat):
    x = 0
    for i in range(len(mat)):
        for j in mat[i]:
            if j == num:
                    x += 1
    return x