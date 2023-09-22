def faltante(l):
    i=1
    for x in l:  
        if x-l[i-1]!=1 or x-l[i-1]!=0:
           	return x-1
        i=i+1
    return i+1