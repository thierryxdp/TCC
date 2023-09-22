def posLetra(s,let,n):
    '''it returns the position of the letter n in s
	string,string,int -> int'''
    ree=[]
    index=0
    while index<len(s):
            if s[index]==let:
	            ree+=[index]
	            index+=1
	        else:
	            index+=1
    if len(ree)<n:
        r=-1
        return r
    else:
        return ree[n-1]