def substitui(s,x,i):
    '''
    '''
	if 0 <= i < len(s):
    	new_s = s[:int(i)]+str(x)+s[int(i+1):]	
    	return new_s