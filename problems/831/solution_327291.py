def lingua_p(palavra):
    '''Retorna uma palavra traduzida para a lingua do P.
    str->str'''
    lingua = ''
    for x in range(len(palavra)):
        if palavra[x] in 'qwrtypsdfghjklçzxcvbnmQWRTYPSDFGHJKLÇZXCVBNM':
            lingua += palavra[x]
        else:
            lingua += palavra[x] + 'p' + palavra[x]
    return lingua