def eh_quadrada(m):
    i = 0
    j = 0
    if len(m) == 1:
        return False
    for x in range(len(m)):
        for y in range(len(m[1])):
            j = j+1
        i = i+1
    if i == j:
        return True
    else:
        return False