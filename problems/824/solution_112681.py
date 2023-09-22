def uppCons (frase):
    '''receb uma frase e retorna a mesma frase com todas as suas consoantes em maisculo e as demais letras exatamente como estavam'''
    '''str->str'''
    i=0
    consoantes=''
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            consoantes=consoantes+frase[i]
            consoantes2= str.upper(consoantes)
            frasefinal= str.replace(frase,consoantes,consoantes2)
        i=i+1
    return consoantes2