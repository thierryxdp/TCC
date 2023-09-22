def uppCons(frase):
    """ str -> str;
    Função que recebe uma frase e retorna a mesma frase,
    porém com suas consoantes em maiúscculas."""
    i = 0
    cons = 'qwrtypsdfghjklçzxcvbnm'
    ret = frase.copy()
    while i < len(frase):
        i = i + 1
        if frase[i] in cons:
            str.upper(ret[i])
    return ret