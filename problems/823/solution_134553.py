def faltante(n): 
    i=0 
    resultado=() 
    while i < len(n)+1: 
        if (int(n[i+1])-int(n[i]))==2:
            resultado=(n[i]+1,)
        i=i+1
    return resultado