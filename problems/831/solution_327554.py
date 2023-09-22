def lingua_p(palavra):
    i=0
    k=''
    while i<len(palavra):
        if palavra[i] in "aeiouAEIOU":
            k=''.join(palavra[i]+'p'+palavra[i])
        i=i+1
    return k