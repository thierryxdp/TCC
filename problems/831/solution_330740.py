def lingua_p(palavra):
    s=[]
    i=0
    while i<len(palavra):
        if palavra[i] in 'aeiou':
            s+=palavra[i]+'p'+palavra[i]
        i+=1
    return s