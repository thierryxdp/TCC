def eh_quadrada(m):
    i = 0
    j = len(m[0])
    if m == [[]]:
        m = m + [1]
    else:
        for x in range(len(m)):
            i = i+1
        if i == j:
            return True
        else:
            return False