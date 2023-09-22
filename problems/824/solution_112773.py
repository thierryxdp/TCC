def uppCons (frase):
    '''receb uma frase e retorna a mesma frase com todas as suas consoantes em maisculo e as demais letras exatamente como estavam'''
    '''str->str'''
    i=0
    a=0
    consoantes=''
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            str.upper(frase[i])
            consoantes=consoantes+frase[i]
        
        elif:
            frase[a] in 'aeiou':
            consoantes=consoantes+frase[a]
        i=i+1
    return consoantes