def lingua_p(palavra):
    l=[palavra]
    i=0
    while i<len(l):
        if l[i] in 'aeiou':
            list.insert(l,i+1,'p')
        i=i+1
    return l