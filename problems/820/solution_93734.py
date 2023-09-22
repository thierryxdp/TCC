def posLetra(string,letra,num):
    i=0
    L=letra
    x=str.count(string,letra)
    while i<len(string):
    	if x<num:
            return -1
        else:
            string.replace('L','',2)
        	return str.index(string,L)
    i=i+1
    return L