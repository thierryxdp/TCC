def uppCons(frase):
    """Essa função recebe uma frase e retona a mesma frase
    como todos as consoantes em maiúsculo
    str->str"""
    
    i = 0
    frase_final = ''
    
    while i<len(frase):        
        if frase[i] in "AEIOUaeiou":
            frase_final = frase_final+frase[i]
        else:
            frase_final = frase_final+ str.upper(frase[i])
        i += 1
    return frase_final