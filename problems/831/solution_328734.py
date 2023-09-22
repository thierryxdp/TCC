def lingua_p(frase):
    """Funcao que receba como parâmetro uma palavra (em portugues) e retorne esta mesma palavra traduzida para a língua do P.
    str -> str"""
    p = ''
    for x in frase:
        if x in 'aeiouáàãâéêóôõú' :
            p = p + x + 'p' + x
        elif x in 'bcdfghjklmnpqrstvwxyzç' :
            p = p + x 
    return str.lower(p)