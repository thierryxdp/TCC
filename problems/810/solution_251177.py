def inverte (l):
    k = ":;!?-,."
    
    for x in l:
        if x in k:
            str.replace(l,x,'')
    return l