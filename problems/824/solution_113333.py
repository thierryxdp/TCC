def uppCons(frase): 
    i=0 
    upcons=''
    while i < len(frase): 
        if frase[i] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ": 
           up= str.upper(frase[i])
        upcons=upcons+(up)
        i=i+1 
    return upcons