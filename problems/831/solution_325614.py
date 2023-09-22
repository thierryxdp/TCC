def lingua_p(v):
    ''' retorna a palavra de entrada na lingua do p
    str -> str'''
    v = str.lower(v)
    a=''
    for b in v:
        a=a+b
        if b in 'aeiou':
            a=a+'p'+b
    return b