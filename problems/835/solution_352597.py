def melhor_volta(x):
    mini=max(x[0])
    
    i=0
    while i<len(x):
        for k in x[i]:
            if k<mini:
                mini=k
                corredor=i
                volta=k
            i=i+1   
	return corredor,mini,volta,