def melhor_volta(mat):
    x = mat[0][0]
    for i in range(len(mat)):
        for j in mat[i]:
            if j < x:
                x = j
                c = i + 1
                v = j + 1
    return (c, x, v)