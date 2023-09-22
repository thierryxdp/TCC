def lingua_p(palavra):
    """recebe uma palavra em português e retorna essa palavra na língua do P.
    str->str"""
    i=0
    p=''
    while i<len(palavra):
        if palavra[i] in 'aeiouáéíóú':
            p=p+palavra[i]+'p'+palavra[i]
        else:
            p=p+palavra[i]
        i=i+1
    return p