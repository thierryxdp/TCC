def melhor_volta(x):
    mini=max(x[0])
    
    i=0
    while i<len(x):
        k=0
        while k<len(x[i]):
            if x[i][k]<mini:
                mini=x[i][k]
                corredor=i
                volta=k
            k=k+1    
        i=i+1   
	return corredor,mini,volta,