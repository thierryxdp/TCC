def lingua_p(palavra):
    '''função que traduz a palavra dada para a língua do P; str -> str'''
    p = str.lower(palavra)
    p_final = ''
    for i in p:
        p_final = p_final + i
        if i in 'aáàâãeéêiíoóôõuú':
            p_final = p_final + 'p' + i
    return p_final