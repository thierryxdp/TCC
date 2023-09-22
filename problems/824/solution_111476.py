def uppCons(frase):
    """Função que receba uma frase e retorne a frase com as suas consoantes em maiúsculas e também a frase original; str-> str,str"""
    i= len(frase) -1
    consoante=''
    while (i>=0 and len(consoante)==0):
        if (str.upper(frase[i]) in 'bcdfghjklmnpqrstvwxyzç'):
            consoante= frase[i]
        i= i-1
    return consoante