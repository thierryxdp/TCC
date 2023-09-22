def repetidos(lista):
    rep=0
    i=1
    while i<len(lista):    	
        if lista[i-1]==lista[i]:
            rep=rep+1
    i=1+i      
    return rep