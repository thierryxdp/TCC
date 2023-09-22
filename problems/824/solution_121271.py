def uppCons(frase):
    """recebe com entrada uma frase e retorna a frase com todas as suas consoantes em maiusculo"""
    a=""
    for i in frase:
        if i not in 'aáãâàeéèêiìíîoòóõôuúùû':
            a+= str.upper(i)
        else:
             if i in 'aáãâàeéèêiìíîoòóõôuúùû':
                 a+= i
    return a