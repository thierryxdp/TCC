def eh_quadrada(m):
    a = [[]]
    i = 0
    j = len(m[0])
    if m == a:
        return True
    for x in range(len(m)):
        i = i+1
    if i == j:
        return True
    else:
        return False