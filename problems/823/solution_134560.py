def faltante(n): 
    i=0 
    y=i+1
    resultado=() 
    while i < len(n)+1: 
        if ((n[y])-(n[i]))==2:
            resultado=(n[i]+1,)
        i=i+1
    return resultado