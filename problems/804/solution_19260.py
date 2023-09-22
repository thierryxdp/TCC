#Start your python function here
#tupla-->tupla
def filtra_pares (t):
    if t[0]%2 != 0:
        t = t[1:4]
        
        if t[0]%2 != 0:
        	t = t[1:3]
       
            if t[0]%2 != 0:
        		t = t[1:2]
                
                if t[0]%2 != 0:
                    t = ()
	return t