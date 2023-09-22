def lingua_p(palavra):
    k=''
    while i<len(palavra):
        if "aeiouAEIOU" in palavra[i]:
            k=palavra[i]+'p'+palavra[i]
    return k