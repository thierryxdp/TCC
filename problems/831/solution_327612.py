def lingua_p(palavra):
    i=0
    k=''
    while i<len(palavra):
        if palavra[i] in "aeiouAEIOU":
            k=k+(palavra[i]+' p '+palavra[i])
        else:
                k=k+palavra[i]
        i=i+1
    return k