def uppCons(frase):
    '''funç̃ao que receba como entrada uma frase e retorne a frase com todas as suas consoantes em
maiúsculas; str -> str'''
    ind=0
    consoantes= ''
    while (ind<len(frase)):
        if frase[ind] in 'bcdfgjklmnpqrstvwxz':
            consoantes=consoantes+frase[ind]
        ind=ind+1

    return str.upper(consoantes)