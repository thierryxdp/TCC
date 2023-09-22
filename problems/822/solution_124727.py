def repetidos(lista):
    numrep=0
    i=1
    while i< len(lista)-1:
        if lista[i] == lista[(i-1)]:
            numrep = numrep+1
    i = i +1	        
    
    return numrep