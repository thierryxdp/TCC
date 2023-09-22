#dado um número int positivo verifica se ele é primo
#int-->bool
def primo(n):
	x=0
	for y in range(2,n):
    	if (n % y == 0):
        	x+=1
	if x==0:
		return True
	else:
		return false