def uppCons (frase):
    '''receb uma frase e retorna a mesma frase com todas as suas consoantes em maisculo e as demais letras exatamente como estavam'''
    '''str->str'''
    i=0
    vogais=''
    vogais1= str.upper(vogais)
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            vogais=vogais+frase[i]
            vogais1= str.upper(vogais)
        i=i+1
    return vogais1