def primo (num):
    '''retorna True se o numero positivo for primo e false caso nao
    int->bool'''
    if num == 1:
        return False
    elif num == 2:
        return True
    counter = 0
    if num > 2:
    	for x in range(num,0,-1):
        	if num%x == 0:
            	counter += 1
        if counter == 2:
            return True
        if counter > 2:
            return False