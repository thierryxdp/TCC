def maiores(lista, n):
    a=[]
    i=0
    
		while lista[i] < n:
        i+=1
        
        if i > n:
            a.append(i)
            a.sort()
    return a