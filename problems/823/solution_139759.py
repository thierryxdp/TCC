def faltante(conjunto):
    
    list.sort(conjunto)
    ordem=list(range(1,len(conjunto)+2))
    
    index=0
    
    while len(ordem) > index:
        if conjunto[index] != ordem[index]:
            return ordem[index]
        
        index= index +1
        
    return ordem[-1]