def conta_numero(numero, matriz):
    l1 = len(mat)
    l2 = len(mat[0])
    count = 0
    for i in range(l1):
        for j in range(l2):
            if mat[i][j] == numero:
                count += 1
   	return count