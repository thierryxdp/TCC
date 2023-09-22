def primo(p):
    m = 1
    n = 1
    while n < p:
        m = m*n
        n = n+1
	return m%p == 0