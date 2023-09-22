def eh_quadrada(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if max[i] == max[j]:
                return True