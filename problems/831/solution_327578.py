def lingua_p(palavra):
    i=0
    p=''
    while i<len(palavra):
        p=''.join('p'+palavra[i]+'p' if vogal in 'aeiouAEIOU' else vogal for vogal in palavra)
    	i=i+1
    return p