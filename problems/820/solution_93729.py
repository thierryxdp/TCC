def posLetra(string,letra,num):
    i=0
    L=letra
    x=str.count(string,letra)
    while i<len(string):
        if x==num:
            string.replace('L','',2)
        	return str.index(string,L)
    	if x<num:
            return -1
    i=i+1
    return L