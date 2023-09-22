def uppCons(frase):
    """funcao que recebe uma frase e retorna a frase com as consoantes em caixa alta"""
    """str->str"""
    i = 0
    
    while i < len(frase):
        if frase[i] != 'aeiou':
        	str.upper(frase[i])
        i = i + 1