def posLetra(string,letra,ocorrencia):
    
    i=0
    
    xtotal=[]

    
    while i<=len(string):
        
        if string[i] in letra:
            x=str.index(string,letra)
            x=str(x)
            xtotal+=xtotal+x
        i+=1
        
        if ocorrencia<=len(xtotal):
            return xtotal
        
        if ocorrencia>len(xtotal):
            return xtotal