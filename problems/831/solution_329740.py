def lingua_p(p):
    '''
    A função recebe uma palavra e a traduz para a 
    linguagem P
    '''
    s = ''
    i = 0
    for x in p:
        i += 1
        s += x
        if x in 'AaáàEeéIiíOoóUuú':
            s += 'p' + x
    return str.lower(s)