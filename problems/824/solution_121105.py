def uppCons(frase):
    """ str -> str;
    Função que recebe uma frase e retorna a mesma frase,
    porém com suas consoantes em maiúscculas."""
    i = 0
    cons = 'qwrtypsdfghjklçzxcvbnm'
    l = list(frase)
    while i < len(l):
        i = i + 1
        if l[i] in cons:
            str.upper(l[i])
    str.join(l, l[0::1]
    return l