def posLetra(string,letra,ocorrencia):
    
    i=0
    
    xtotal=[]

    
    while i<=len(string):
        
        if string[i] in letra:
            x=str.index(string,letra)
            xtotal.append(x)
            i+=1
        
        if ocorrencia<=len(xtotal):
            return xtotal(ocorrencia)
        
        if ocorrencia>len(xtotal):
            return -1