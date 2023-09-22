def uppCons(frase):
    """ str -> str;
    Função que recebe uma frase e retorna a mesma frase,
    porém com suas consoantes em maiúscculas."""
    ret = frase.copy()
    for e in ret:
        if e not in 'AEIOUaeiou':
            ret.upper()
    return ret