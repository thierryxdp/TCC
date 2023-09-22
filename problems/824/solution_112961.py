def uppCons(frase):
    '''funcao que retorne a frase com todas as consoantes em maiusculas'''
    i=0
    consoante=[]
    while i<len(frase):
        if frase[i]in 'BCDFGHJKLMNPQRSTVXWYZ,bcdfghjklmnpqrstvxwyz':
            str.upper(frase[i])
        i=i+1
    return frase