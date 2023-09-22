def eh_quadrada(m):
    i = 0
    j = 0
    if m == [[]]:
        m = 0
    for x in range(len(m)):
    	i = i+1
    for y in range(len(m[0])):
        j = j + 1        
    if i == j:
        return True
    else:
        return False