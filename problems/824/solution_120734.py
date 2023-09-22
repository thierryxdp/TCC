def uppCons(x):
    n = 0
    string = ''
    while n<len(x):
        if x[n] not 'aeiouAEIOU' :
            x[n]=x[n].upper()
        n = n+1
        string = string+str(x[n])
        
    return string