def lingua_p(palavra):
    i=0
    p=[]
    while i<len(palavra):
        if palavra[i] in 'aeiouAEIOU':
            p.append(palavra[i]+'p'+palavra[i])
    return p