def uppCons(frase):
    """Função que retorna a frase de entrada com todos as suas
    consoantes em maiúsculas. str -> str"""
    
    i = 0
    s = ''
    
    while i < len(frase):
        if frase[i] in 'aeiouAEIOU':
            s = s + frase[i]
            i+= 1
        elif frase[i] in 'bcdfghjklmnpqrstvwxyz':
            s = s + str.upper(frase[i])
            i+= 1
        return s