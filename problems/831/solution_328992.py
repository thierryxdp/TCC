def lingua_p(h):
    '''traduz para a língua do p; str -> str'''
    k = str.lower(h)
    samara = ''
    for i in range(len(k)):
        if k[i] in 'aeiou':
            samara += k[i] + 'p' + k[i]
        elif k[i] not in 'aeiou':
            samara += k[i]
    return samara