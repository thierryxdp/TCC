def uppCons(frase):
    """Função que receba uma frase e retorne a frase com as suas consoantes em maiúsculas e também a frase original; str-> str,str"""
    i= len(frase)
    consoante=''
    while (len(consoante)==0):
        if (consoante) in 'bcdfghjklmnpqrstvwxyzç'):
            consoante= frase.upper()
        i= i+1
    return consoante