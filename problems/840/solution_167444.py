def bolos(a, b, c):
    acc = 0
    while True:
        xicaras = a - 2
        ovos = b - 3
        leite = c - 5
    	if xicaras < 0 or ovos < 0 or leite < 0:
            acc += 1
            break
        return acc