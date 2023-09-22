def lingua_p(palavra):
    i=0
    p=''
    while i<len(palavra):
        if palavra[i] in 'aeiouAEIOUáéíóú':
            p=p+(palavra[i]+'p'+palavra[i])
        else:
            p=p+palavra[i]
        i=i+1
    return p