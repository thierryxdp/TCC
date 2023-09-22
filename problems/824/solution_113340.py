def uppCons(frase): 
    i=0
    upcons=''
    while i < len(frase): 
        if frase[i] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ": 
            upcons=upcons+ str.upper(frase[i]) 
        if frase[i] not in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ": 
            umpcons=upcons+(frase[i])
        i=i+1
    return upcons