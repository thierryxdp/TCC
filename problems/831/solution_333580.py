def lingua_p(palavra):
    p=palavra.lower()
    s=''
    for c in p:
        if c in 'AEIOUaáàãâeéèêiíìîoóòõôu':
            s+=c+'p'+c
        else:
            s+=c
    return s