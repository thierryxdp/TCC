def uppCons(frase):
    """ str -> str;
    Função que recebe uma frase e retorna a mesma frase,
    porém com suas consoantes em maiúscculas."""
    ret = ""
    cons = 'qwrtypsdfghjklzxcvbnmç'
    for e in frase:
        if e in cons:
            for e in frase:
                frase = str.upper(e) in frase
    ret = frase
    return frase