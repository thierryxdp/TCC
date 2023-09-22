def melhor_volta(m):
    min_c = []
    i = 0
    while i < len(m):
        list.append(min_c, min(m[i]))
        i = i+1
        for k in range(len(m)):
            for j in range(len(m[0])):
                if min(min_c) == m[k][j]:
                    return k+1, m[k][j], j+1