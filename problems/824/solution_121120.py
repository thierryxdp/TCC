def uppCons(frase):
    """ str -> str;
    Função que recebe uma frase e retorna a mesma frase,
    porém com suas consoantes em maiúscculas."""
    ret = ""
    cons = 'qwrtypsdfghjklzxcvbnmç'
    for e in frase:
        if e in cons:
            str.upper(e)
    ret = frase
    return ret