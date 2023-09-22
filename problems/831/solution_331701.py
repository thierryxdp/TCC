def lingua_p (palavra):
    '''função que dada uma palavra em portugues retorna a mesma na lingua do p;
    str->str'''
    string = str.lower(palavra)
    i=0
    lp = ''
    for letra in string:
        if letra in 'aeiou':
            lp = lp[i:] + 'p' + lp[:i]
        else:
            lp = lp
        i += 1
    return lp