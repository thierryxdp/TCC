def uppCons(x):
    r=[]

    i=0
    while i<len(x):
        if x[i] in ["a","e","i","o","u"]:
            return x[i]
        return str.upper(x[i])
        r+=x[i]
        i+=1
            
    return r