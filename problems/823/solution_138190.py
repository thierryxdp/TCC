def faltante(lst):    
    i = 0
    numFaltante = 1
    while i <= (len(lst))+1:
        if numFaltante == (len(lst))+1:
            return numFaltante
        
        elif numFaltante != lst[i]:
            return numFaltante
        
        numFaltante += 1
        i += 1