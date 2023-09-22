def lingua_p(palavra):
    k=''
    i=0
    while i<len(palavra):
        if "aeiouAEIOU" in palavra[i]:
            k=k.join(palavra[i]+'p'+palavra[i])
        i=i+1
    return k