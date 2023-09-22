def posLetra(string,letra,ocorrencia):
    
    i=0
    
    xtotal=''

    
    while i<len(string):
        
        if string[i] in letra:
            x=str.index(string,letra)
            return x
        i+=1