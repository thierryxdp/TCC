#Questao 3
def lingua_p(palavra):
    '''
    funcao que retorna a palavra traduzida na lingua p.
    str->str.
    '''
    t = ''
    for x in range(len(palavra)):
        if palavra[x] in 'qwrtypsdfghjklçzxcvbnmQWRTYPSDFGHJKLÇZXCVBNM':
            t = t + palavra[x]
        else:
            t = t + palavra[x] + 'p' + palavra[x]
    return t