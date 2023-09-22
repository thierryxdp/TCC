def uppCons (frase):
    '''receb uma frase e retorna a mesma frase com todas as suas consoantes em maisculo e as demais letras exatamente como estavam'''
    '''str->str'''
    um=str.replace (frase, 'b','B')
    dois=str.replace (um, 'c','C')
    tres=str.replace (dois, 'd','D')
    return tres