def inverte(l):
    g='?-!;:,.'
    
    for x in g:
        if (x in l)==True:
            str.replace(l,x,'')
     
    return l