def media_matriz(mat):
    qnt = 0
    summ = 0

    for l in mat:
        for el in l:
            summ += el
            qnt += 1

    return round(summ/qnt, 2)