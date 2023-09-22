def uppCons(frase): 
    i=0
    upcons=''
    while i < len(frase): 
        if frase[i] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ": 
            upcons=upcons+ str.upper(frase[i]) 
        else:
            if frase[i] in "!?,.- aãáâeéêíióôoõuAÃÁÂÉÊEIÍOÔÕÓU": 
                upcons=upcons+(frase[i])
        i=i+1
    return upcons