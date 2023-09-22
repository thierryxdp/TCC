def uppCons(frase):
    """Essa função recebe uma frase e retona a mesma frase
    como todos as consoantes em maiúsculo
    str->str"""
    
    i = 0
    frase_final = ''
    
    consoantes = 'bcçdfghjklmnpqrstvwxyz'
    consoantes = consoantes + str.upper(consoantes)
    
    while i<len(frase):        
        if frase[i] not in consoantes:
            frase_final = frase_final+frase[i]
        else:
            frase_final = frase_final+ str.upper(frase[i])
        i += 1
    return frase_final