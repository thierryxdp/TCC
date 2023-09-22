def uppCons(frase):
    """ str -> str;
    Função que recebe uma frase e retorna a mesma frase,
    porém com suas consoantes em maiúscculas."""
    i = 0
    cons = 'qwrtypsdfghjklçzxcvbnm'
    l = list(frase)
    while i < len(l):
        if l[i] in cons:
            str.upper(l[i])
        i = i + 1
    str.join('a', l)
    return l