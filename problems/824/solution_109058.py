def uppCons(frase):
    '''função que dada uma frae em string, retorna essa frase com suas consoantes
       em maiúsculo, não modificando outros caractéres. str -> str'''
    pos = 0
    while pos < len(frase):
        if frase[pos] in 'bcdfghjklmnpqrstvwxyz':
            frase_upper = str.upper(frase[pos])
            str.replace(frase, frase[pos], frase_upper)
        pos = pos + 1
    return frase