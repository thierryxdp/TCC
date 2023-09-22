def uppCons(x):
    r=[]

    i=0
    while i<len(x):
        if x[i] in ["a","e","i","o","u"]:
            r.append(x[i])
        r.append(str.upper(x[i]))
        i+=1
            
    return "".join(r)