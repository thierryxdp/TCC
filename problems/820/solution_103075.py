def posLetra(string,letra,ocorrencia):
    
    i=0
    
    xtotal=''

    
    while i<=len(string):
        
        if string[i] in letra:
            x=str.index(string,letra)
            xtotal=xtotal+x
        i+=1
        
        elif ocorrencia<=len(xtotal):
            return xtotal[ocorrencia]
        
        elif ocorrencia>len(xtotal):
            return -1