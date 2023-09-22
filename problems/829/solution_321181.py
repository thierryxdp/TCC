def soma_h(n):
	i = 0
    for n1 in range(1, n + 1):
        fat = 1
        for n2 in range(n1, 0, -1):
            fat = 1/fat
        i = i + 1
    return i