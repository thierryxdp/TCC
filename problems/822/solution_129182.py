def repetidos(ls):
    c=0
    a=0
    while c<len(ls):
        if ls[c]==ls[c+1]:
            a+=1
    	c+=1
    return a