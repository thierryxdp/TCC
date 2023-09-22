def melhor_volta(m):
    min_c = []
    lin = 0
    col = 0
    while lin < len(m):
        list.append(min_c, min(m[lin]))
        lin = lin + 1
        while col < len(m[0]):
            if min(min_c) == m[lin][col]:
                return lin+1, m[lin][col], col+1
            col = col + 1