def uppCons(frase):
    """ str -> str;
    Função que recebe uma frase e retorna a mesma frase,
    porém com suas consoantes em maiúscculas."""
    ret = list(frase)
    for e in ret:
        if e in 'qwrtypsdfghjklçzxcvbnm':
            e.upper()
    str.join('', ret[0::1])
    return ret