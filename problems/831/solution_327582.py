def lingua_p(palavra):
    i=0
    p=''
    while i<len(palavra):
        p=''.join('p'+palavra[i]+'p' if x in 'aeiouAEIOU' else x for x in palavra)
    	i=i+1
    return p