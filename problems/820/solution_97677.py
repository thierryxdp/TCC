def posLetra(string,letra,numero):
    """
    
    
    """
    vezes_encontradas=0
    i=0
    if str.find(string,letra)>= numero:
        while i<len(string):
        if i!=i:
            if string[i]==letra:
                vezes_encontradas= vezes_encontradas + 1
                
        i=i+1
    return vezes_encontradas    
    elif str.find(string,letra)< numero or str.find(string,letra)==-1:
        return -1