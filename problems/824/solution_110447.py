def uppCons(frase):
    """Dada a frase de entrada, retorna a mesma frase com todas as consoantes em maiuscolo;
    str -> str"""
    
    indice = 0
    
    while frase[indice] in 'bcçdfghjklmnpqrstvwxyz':
        return str.upper(frase[indice])
    indice += 0