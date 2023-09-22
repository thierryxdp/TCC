#Start your python function here
#tupla-->tupla
def filtra_pares (t):
    if t[0]%2 != 0:
        'impar'
        t = t[1:4]
        
        if t[1]%2 != 0:
        	t = t[2:4]
            
            if t[2]%2 != 0:
        		t = t[3:4]
                if t[0]%2 != 0:
                    t = []
	return t