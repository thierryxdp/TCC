def primo(n):
    for x in range(2,((n)**(1/2))+1):
        if n%x==0:
            return False
	return True