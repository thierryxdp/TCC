def lingua_p(palavra):
    l=[palavra]
    if i<len(l):
        if l[i] in 'aeiou':
            list.insert(l,i,'p')
    return l