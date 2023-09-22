def posLetra(string,letra,ocorrencia):
    
    i=1

    
    while string[i] in letra:
        x=str.index(string,letra)
        i+=1
        
        if i==ocorrencia:
            return x
        
        else:
            return -1