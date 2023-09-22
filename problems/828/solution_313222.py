def primo(n):
		quantidade=0
    	for numero in range(1,n+1):
        	if n%numero==0:
        		quantidade=quantidade+1
    		if quantidade>2:
        		return False
    		elif quantidade<=2:
        		return True