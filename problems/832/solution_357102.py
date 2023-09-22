def eh_quadrada(m):
    a = [[]]
    i = 0
    if m == a:
        return True
    j = len(m[0])
    for x in range(len(m)):
        i = i+1
    if i == j:
        return True
    else:
        return False