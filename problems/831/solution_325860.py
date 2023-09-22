def lingua_p(palavra):
    l=[palavra]
    for i in range(l):
        if l[i] in 'aeiou':
            list.insert(l,i,'p')
    return l