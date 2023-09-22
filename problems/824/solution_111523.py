def uppCons(frase):
    """Função que receba uma frase e retorne a frase com as suas consoantes em maiúsculas e também a frase original; str-> str,str"""
    i= 0
    consoante=''
    while (i<len(frase)):
            if frase[i] not in 'aeiouAEIOU':
            	consoante=consoante+str.upper(frase[i])
            else:
            	consoante=consoante+frase[i]
    return consoante