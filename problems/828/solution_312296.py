def totalDivisores(n):
	total=0
    for x in range(n):
        if n%(x+1)==0:
            total+=1
    return total

def primo(n):
	return not totalDivisores(n)>2