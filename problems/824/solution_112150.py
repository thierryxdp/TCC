def verificaCaracter(c):
    if c in 'bcddfghjklmnpqrstvwxyzç':
        return c.upper()
    else:
        return c

def uppCons(frase):
    fraseAlterada = str.join(
        '',
        map(verificaCaracter,frase)
    	)
    return fraseAlterada