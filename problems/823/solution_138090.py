def faltante(lis):
    
    falta= len(lis)+ 1
    N= 1
    i= 0
    while i <= falta:
        
        if N == falta:
            return N
        
        elif N != lis[i]:
            return N
        N+= 1
        i+=1