def verificaCaracter(c):
    
    vogais = ['a', 'e', 'i', 'o', 'u']
    
    return str.upper(c) if c not in vogais else c

def uppCons(frase):
    
    fraseAlterada = map(verificaCaracter, frase)
    
    return fraseAlterada