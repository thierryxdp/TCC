def uppCons(x):
    """Recebe uma frase e retorna a frase com todas as suas 
    consoantes em maiúsculas.
    assinatura str -> str
    """ 
    a = ''
    for i in x:
        if i in 'bcdfghjklmnpqrstvxwzç':
            a +=str.upper(i)
        else:
            a += i
    return a