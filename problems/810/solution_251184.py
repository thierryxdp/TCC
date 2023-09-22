def inverte(l):
    ''' '''
    f="?!;:-,."
    
    for x in f:
        if (x in l)==True:
            list.replace(l,x,'')
    
    return l