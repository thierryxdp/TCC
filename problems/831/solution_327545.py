def lingua_p(palavra):
    i=0
    k=''
    while i<len(palavra):
        if "aeiouAEIOU" in palavra[i]:
            k=palavra[i]+'p'+palavra[i]
        return k