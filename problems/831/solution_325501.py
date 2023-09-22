def lingua_p(frase):
    resultado=''
    for palavra in frase:
        if palavra in 'bcdfghjklmnpqrstvwxyz':
            x=str.lower(palavra)
            resultado=resultado+x
        if palavra not in 'bcdfghjklmnpqrstvwxyz':
            x=str.lower(palavra)
            resultado=resultado+ x+str('p')+x
    return resultado