def lingua_p(x):
    i=0
    s=''
    while i < len(x):
        if i in 'aeiouAEIOU':
            s+(i+p+i)
        else:
            s+i
    return s