def eh_quadrada(m):
    i = 0
    j = len(m[0])
    if len(m) == 0:
        return True
    for x in range(len(m)):
        i = i+1
    if i == j:
        return True
    else:
        return False