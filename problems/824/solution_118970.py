def uppCons(frase):
    """Funcao que retorna a frase de entrada com
    todas as consoantes maiusculas"""
    i=0
    while i<len(frase):
        if frase[i]in 'bcdfghjklmnpqrstvxwyz':
            str.upper(frase[i])
        i=i+1
    return frase