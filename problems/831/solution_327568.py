def lingua_p(palavra):
    i=0
    k=''
    while i<len(palavra):
        if palavra[i] in "aeiouAEIOU":
            k=(palavra[i]+'p'+palavra[i])
        i=i+i
    return k