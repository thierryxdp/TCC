def eh_quadrada(m):
    i = 0
    if m == [[]]:
        return True
    for x in range(len(m)):
    	i = i+1
    j = len(m[0])
    if i == j:
        return True
    else:
        return False