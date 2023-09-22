def primo(int_Pos):
    divisores = 0
    
    for divisor in range(1,int_Pos+1):
        if (int_Pos % divisor) == 0:
            divisores += 1
        	if (divisores >= 2):
            	return False
        	else: 
            	return True