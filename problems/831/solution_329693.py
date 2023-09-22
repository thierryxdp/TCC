def lingua_p(palavra):
    """recebe uma palavra em português e retorna essa palavra na língua do P.
    str->str"""
    p=''
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouáéíóú':
            p=p+palavra[i]+'p'+palavra[i]
        else:
            p=p+palavra[i]
    return p