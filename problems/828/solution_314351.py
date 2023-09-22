def primo(n:int)-> bool:
    if n>=2:
    	for i in range(2,n):
        	if not(n%i):
          		return False
    else:
    	return False
    return True