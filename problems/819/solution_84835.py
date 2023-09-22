def filtraMultiplos(ls,n):
    soma = []
    
    i = 0
    while i < len(ls):
    	if ls[i]%n==0: 
            
            soma.append(ls[i])
            soma =[ls[i]]
    		i = i + 1
        else:
            i = i + 1
	return soma