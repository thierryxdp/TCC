def uppCons(frase): 
    i=0 
    upcons=''
    while i < len(frase): 
        if frase[i] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ": 
            letra = str.upper(frase[i])
        upcons=upcons+(letra)
        i=i+1 
    return upcons