def lingua_p(p):
    '''Essa função ao receber como valor de entrada uma string(em português), ela retornara esta mesma palavra traduzida para a língua do P'''
    ''' str->str'''
    m = str.lower (p)
    v = 'aeiouáéíóúâêôãõ'
    f= ''
    for l in m:
        if l in v:
            f+= l + 'p' +l
        else:
            f += l
            
    return f