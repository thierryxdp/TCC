def uppCons(x):
    c=0
    f=''
    while c<len(x):
        if x[c] in ('A','E','I','O','U','a','e','i','o','u'):  
            return x[c]
            
        return str.upper(x[c])