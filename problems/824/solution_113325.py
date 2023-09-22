def uppCons(frase): 
    i=0 
    upcons=() 
    while i < len(frase): 
        if frase[i] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ": 
           str.upper(frase[i])
        upcons=(upcons)+(frase[i])
        i=i+1 
    return upcons