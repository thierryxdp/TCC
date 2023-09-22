def uppCons(frase):
    """ str -> str;
    Função que recebe uma frase e retorna a mesma frase,
    porém com suas consoantes em maiúscculas."""
    i = 0
    cons = 'qwrtypsdfghjklzxcvbnmç'
    l = list(frase)
    lret = []
    while i < len(l):
        i = i + 1
        lret = l.append(l[i])
        if l[i] in cons:
            str.upper(l[i])
            i = i + 1
    s = str.join('', lret)
    return s