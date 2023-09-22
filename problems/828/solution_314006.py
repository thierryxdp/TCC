def primo(n):
    b=True
	for i in range(n-1):
		if n%(i+1)==0:
			b=False
	return b