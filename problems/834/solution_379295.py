def media_matriz(m):
    '''recebe uma matriz e retorna a média dos elementos
    presentes
    list(list)->float'''
    nume = 0
    deno = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            nume = nume + m[i][j]
            deno += 1
    return round((nume/deno),2)