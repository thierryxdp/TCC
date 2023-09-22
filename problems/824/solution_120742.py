def uppCons(x):
    n = 0

    string = ''
    while n<len(x):
        if x[n] in 'bcdfghjklmnpqrstvwxyz' or 'bcdfghjklmnpqrstvwxyz'.upper():
            string = string + x[n].upper()
        else:
            string = string + x[n]
        
        n = n+1
        
        
    return string