def inverte (l):
    k = ':;!?-,.'
    
    for x in k:
        if x in l:
            str.replace(l,x,'')
    return l