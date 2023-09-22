def lingua_p(palavra):
    i=0
    k=''
    k2=''
    while i<len(palavra):
        if palavra[i] in "aeiouAEIOU":
            k=(palavra[i]+'p'+palavra[i])
        i=i+1
        else:
            k2=palavra[i]
    return k+k2