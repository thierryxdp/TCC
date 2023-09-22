def uppCons(frase):
    """Função que dada uma frase retorne a mesma com 
       suas consoantes em caixa alta e os demais 
       caracteres como estavam na frase original.
       str->str"""
    i = 0
    while i < len(frase):
        caractere = frase[i]
        if caractere in 'bcdfghjklmnpqrstvwxyz':
            caractere1 = str.upper(caractere)
            frase = str.replace(frase,caractere,caractere1)
        i = i + 1
    return frase