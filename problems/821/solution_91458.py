def fatorial(x):
    n = 0
    y = 0
    while n < x:
        n += 1
        y += x*(x - n)
	return y