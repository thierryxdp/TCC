def posLetra(string, letra, numero):
    a=str.count(string,letra)
    if a-numero<0:
        return -1
    else:
        b=str.find(string,letra)
    	return b