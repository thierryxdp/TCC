def lingua_p(x):
    '''Retorna uma palavra na língua do p.
    str -> str'''
    x=list(x)
    nl=[]
    i=0
    while i<len(x):
        if 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'O' or 'U' not == x[i]:
            nl.append(i)
    	elif 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'O' or 'U' == x[i]:
            nl.append('p'+i+'p')
        else:
            nl=nl
    return nl