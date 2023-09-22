def uppCons(frase):
    """Função que receba uma frase e retorne a frase com as suas consoantes em maiúsculas e também a frase original; str-> str,str"""
    i= 0
    consoante=''
    while (len(frase)==0):
        if (frase in 'bcdfghjklmnpqrstvwxyzç'):
            consoante=consoante.upper
        i= i+1
    return consoante