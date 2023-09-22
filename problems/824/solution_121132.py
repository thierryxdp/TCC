def uppCons(frase):
    """ str -> str;
    Função que recebe uma frase e retorna a mesma frase,
    porém com suas consoantes em maiúscculas."""
    ret = ""
    vogal = 'AEIOUaeiou'
    cons = 'qwrtypsdfghjklzxcvbnmç'
    for e in frase:
        if e in cons:
            ret = ret + str.upper(e)
        else:
            ret = ret + e
    return ret