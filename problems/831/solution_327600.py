def lingua_p(palavra):
    i=0
    p=[]
    while i<len(palavra):
        if palavra[i] in 'aeiouAEIOU':
            p=p+(palavra[i]+'p'+palavra[i])
        i=i+1
    return 'p'