def primo(p):
    m = 0
    n = 0
    while n < p:
        m = m*n
        n = n+1
	return m%p == 0