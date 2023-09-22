def media_matriz(mat):
    if mat == []:
        return 0
    else:
        l2 = len(mat[0])
    l1 = len(mat)
    
    soma = 0
    n_items = 0
    for i in range(l1):
        for j in range(l2):
            soma += mat[i][j]
            n_items += 1
    
    media = soma/n_items
    
    return round(media,2)