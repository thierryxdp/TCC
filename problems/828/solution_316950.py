def primo(N):
 
    for i in range((2),(N)):
        if N%i== 0:
        	return False
        i+=1
    return True