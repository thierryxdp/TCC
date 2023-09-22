def posLetra(string,letra,num):
    resultado=1
    i=0
    x=str.count(string,letra)
    while i<len(string):
        if x!=num:
        	return -1
        if x>=2:
        	y=str.find(string,letra)
    i=i+1
    return resultado