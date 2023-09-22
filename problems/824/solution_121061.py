def uppCons(frase):
    """ str -> str;
    Função que recebe uma frase e retorna a mesma frase,
    porém com suas consoantes em maiúscculas."""
    for e in frase:
        if e not in 'AEIOUaeiou':
            e.upper()
    return frase