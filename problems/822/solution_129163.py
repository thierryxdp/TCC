def repetidos(listanum):
    quant=0
    n=0
    tamlist=len(listanum)
    
    while quant<tamlist:
        if quant>0 and listanum[quant]==listanum[quant-1]:
            n=n+1
        
        quant=quant+1
    return n