def uppCons(frase):
    """ str -> str;
    Função que recebe uma frase e retorna a mesma frase,
    porém com suas consoantes em maiúscculas."""
    ret = ''
    for e in ret:
        if e in 'qwrtypsdfghjklçzxcvbnm':
            ret.append(str.upper(e))
        else:
            ret.append(e)
    return ret