def lingua_p(palavra):
    i=0
    k=''
    while i<len(palavra):
        if palavra[i] in "aeiouAEIOU":
            k=(palavra[i]+'p'+palavra[i])
            j=k
            l=j+k
        i=i+1
    return k