def uppCons (frase):
    """Função que recebe de emtrada um frase e retorna a frase com as suas consoantes em maiúsculas"""
    """string -> string"""
    
    i = 0
    retorno = ' '
    
    while i < len(frase):
        frasecons = frase[i]
        if frasecons in 'bcdfghjklmnpqrstvwxyzç':
        frasecons = str.upper(frasecons)
        retorno = retorno + frasecons
        i = i + 1
        
    return retorno