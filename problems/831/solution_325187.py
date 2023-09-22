# Língua do P
def lingua_p(palavra):
    '''Essa função recebe uma palavra em português e a traduz para a
    língua do P;
    STR -> STR'''
    pv = palavra.lower()
    l = []
    for i in pv:
        if i in 'bcdfghjklmnpqrstvwxyzç':
            l.append(i)
        else:
            l.append(i)
            l.append('p')
            l.append(i)
    return ''.join(l)