#Start your python function here
def filtra_pares(t):
    "essa função retonrna valores pares de uma tupla"
	if t[0]%2==0:
        a=t[0]
    else:
    	a=0
    if t[1]%2==0:
        b=t[1]
    else:
    	b=0
    if t[2]%2==0:
        c=t[2]
    else:
    	c=0
	if t[3]%2==0:
        d=t[3]
    else:
    	d=0
        
    if a==0:
        
    	if b==0:
            
            if c==0:
                if d==0:
                    t1=()
                else :
                    t1=(d)
                
            else:
                if d==0:
                    t1=(c)
                else :
                    t1=(c,d)
                
        else
        	if c==0:
                if d==0:
                    t1=(b)
                else :
                    t1=(b,d)
                
            else:
                if d==0:
                    t1=(b,c)
                else :
                    t1=(b,c,d)
                
            	
    else:
        if b==0:
            
            if c==0:
                if d==0:
                    t1=(a)
                else :
                    t1=(a,d)
                
            else:
                if d==0:
                    t1=(a,c)
                else :
                    t1=(a,c,d)
                
        else
        	if c==0:
                if d==0:
                    t1=(a)
                else :
                    t1=(a,b,d)
                
            else:
                if d==0:
                    t1=(a,b,c)
                else :
                    t1=(a,b,c,d)
                
        
    return t1