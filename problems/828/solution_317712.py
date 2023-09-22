def primo (n):
    multiplos = 0
    for i in range (2,n//+1):
        if n % i !=0: 
            multiplos += 0
        else: 
            multiplos += 1
	if multiplos == 0:
        return True
    else:
        return False