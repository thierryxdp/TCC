def lingua_p(palavra):
    '''Dado uma palavra, introduz a letra p apos cada vogal e repete a vogal.str->str.'''
    i=0
    k=''
    while i<len(palavra):
        if palavra[i] in "aeéiouáúAEIOU":
            k=k+(palavra[i]+'p'+palavra[i])
        else:
                k=k+palavra[i]
        i=i+1
    return k