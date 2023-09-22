def primo(x):
    n=0
    for y in range (2,x+1):
        if x%y==0:
        	n=n+1
    if n==2:
    	return True
    else:
        return False