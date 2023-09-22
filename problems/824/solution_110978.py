def uppCons(frase):
    """Função que dada uma frase retorne a mesma com 
       suas consoantes em caixa alta e os demais 
       caracteres como estavam na frase original.
       str->str"""
    frase = ''
    i = 0
    while i < len(frase):
        caractere = frase[i]
        if caractere in 'bcdfghjklmnpqrstvwxyz':
             frase = frase + frase[frase.index(caractere)]=str.upper(caractere)
        i = i + 1
    return frase