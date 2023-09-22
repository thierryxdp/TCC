def verificaCaracter(c):
    
    vogais = ['a','á','â','ã','à', 'e','é','ê', 'i','í','î', 'o','ó','ô','õ', 'u','ú']
    
    return str.upper(c) if c not in vogais else c

def uppCons(frase):
    
    fraseAlterada = str.join('',map(verificaCaracter, frase))
    
    return fraseAlterada