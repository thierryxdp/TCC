def lingua_p(palavra):
    '''Funcao que, dada uma palavra, retorna essa palavra na lingua do p, ou seja, apos cada vogal, e inserido o p e em seguida a propria vogal; str -> str'''
    str.lower(palavra)
    str.split(palavra)
    i=0
    while i<len(palavra):
        if palavra in 'aeiou':
            list.insert(palavra,i,'p'+palavra)
        i=i+1
        return palavra