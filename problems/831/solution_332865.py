def lingua_p(x):
    i=0
    s=''
    while i < len(x):
        if x[i] in 'aeiouAEIOUáéú':
            s+=(x[i]+'p'+x[i])
        else:
            s+=x[i]
        i+=1
    return s