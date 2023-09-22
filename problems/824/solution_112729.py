def uppCons (frase):
    '''receb uma frase e retorna a mesma frase com todas as suas consoantes em maisculo e as demais letras exatamente como estavam'''
    '''str->str'''
    um=str.replace (frase, 'B','b')
    dois=str.replace (um, 'C','c')
    tres=str.replace (dois, 'D','d')
    return tres