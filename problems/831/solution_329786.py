def lingua_p(palavra):
    '''Funcao que, dada uma palavra, retorna essa palavra na lingua do p, ou seja, apos cada vogal, e inserido o p e em seguida a propria vogal; str -> str'''
    str.lower(palavra)
    i=0
    nova=''
    while i<len(palavra):
        if palavra[i] in 'aeiou':
            nova=palavra[i]+'p'+palavra(i)
        else:
            nova=palavra[i]
        i=i+1
    return nova