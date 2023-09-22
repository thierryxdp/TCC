def lingua_p(palavra):
    '''função que dado uma palavra retorna
    a mesma traduzida para a língua do P. str -> str '''
    p = str.lower(palavra)
    r = '' ''
    for i in range(0, len(p)):
        if p [i] not in "aeiouáéú":
            r = r + p[i]
        if p [i] in "aeiouáéú":
            r = r + p[i] + "p" + p[i]
    return r