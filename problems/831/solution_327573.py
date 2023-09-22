def lingua_p(palavra):
    i=0
    k=''
    while i<len(palavra):
        if palavra[i] in "aeiouAEIOU":
            k=''.join('p'+palavra[i]+'p' if vogal in 'aeiouAEIOU' else vogal for vogal in palavra)
        i=i+1
    return k