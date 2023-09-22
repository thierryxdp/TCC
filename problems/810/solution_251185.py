def inverte(l):
    ''' '''
    f="?!;:-,."
    
    for x in f:
        if (x in l)==True:
            str.replace(l,x,'')
    
    return l