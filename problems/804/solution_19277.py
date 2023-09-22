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
	else:
        if t[1]%2 != 0:
        	t = t(0)+t(2:4)
       
            if t[1]%2 != 0:
        		t = t[0] + t[2:3]
                
                if t[1]%2 != 0:
                    t = t[0]
        else:
			if t[2] % 2 != 0:
            	t = t[0:2] + t[3]
                if t[3] % 2 != 0:
                    t = t[0:2]
            else:
            	if t[3] % 2 != 0 :
                	t = t[0:3]   
	return t