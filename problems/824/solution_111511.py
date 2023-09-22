def uppCons(frase):
    """Função que receba uma frase e retorne a frase com as suas consoantes em maiúsculas e também a frase original; str-> str,str"""
    i= 0
    while (i<len(frase)):
           if frase[i] not in 'aeiouAEIOU':
            s=s+str.upper(frase[i])
            else:
            s=s+frase[i]
    return s