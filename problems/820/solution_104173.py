def posLetra(s,let,n):
    '''it returns the position of the letter n in s
	string,string,int -> int'''
    ree=[]
    index=0
    while len(ree)<n:
        
        index=0
	    while index<len(s):
            if s[index]==let:
	            ree+=[index]
	            index+=1
	        else:
	            index+=1
	r=ree[n]
    if len(ree)==0:
        r=-1
    return r