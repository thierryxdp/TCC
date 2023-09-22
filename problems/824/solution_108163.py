def uppCons(frase):
    """Função que retorna a frase de entrada com todos as suas
    consoantes em maiúsculas. str -> str"""
    
    indice = 0
    s = ''
    
    while indice < len(frase):
        if frase[indice] in 'aeiou':
            s = s + frase[indice]
        elif frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            s = s + str.upper(frase[indice]
        
    return s