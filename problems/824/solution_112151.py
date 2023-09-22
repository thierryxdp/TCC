def verificaCaracter(c):
    "Recebe um caracter, se o caracter for uma consoante retorna ela em maiusculo, se não for retorna como entrou"
    if c in 'bcddfghjklmnpqrstvwxyzç':
        return c.upper()
    else:
        return c

def uppCons(frase):
    "Recebe uma frase e retorna a mesma com suas consoantes maiusculas"
    fraseAlterada = str.join(
        '',
        map(verificaCaracter,frase)
    	)
    return fraseAlterada