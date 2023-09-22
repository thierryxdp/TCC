def uppCons(frase):
    """Função que receba uma frase e retorne a frase com as suas consoantes em maiúsculas e também a frase original; str-> str,str"""
    i= 0
    consoante=''
    while (len(consoante)==0):
        if (consoante in 'bcdfghjklmnpqrstvwxyzç'):
            consoante= (consoante-frase)
        i= i+1
    return consoante