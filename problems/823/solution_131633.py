def faltante(l):
    
    l.sort()
    
    i =1
    if  l[0] != 1:
        return 1
    while i< len (l):
        if(l[i] - l[i-1]) != 1:
            return int ((l[i] + l[i-1])/2)
        i=i+1
        
        if l[0] == 1:
            return l[-1] +1