def posLetra(string,letra,ocorrencia):
    
    i=0
    
    xtotal=''

    
    while i<=len(string):
        
        while string[i] in letra:
            x=str.index(string,letra)
            xtotal=xtotal+x
        i+=1
        
        if ocorrencia<=len(xtotal):
            return xtotal
        
        if ocorrencia>len(xtotal):
            return xtotal