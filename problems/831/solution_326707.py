def lingua_p (palavra):
    ling_p = ''
    for i in range (len(palavra)):
        if palavra[i] in 'AEIOUaeiou':
            ling_p += palavra[i]+'p'
        else:
            ling_p += palavra[i]
    return ling_p.lower()