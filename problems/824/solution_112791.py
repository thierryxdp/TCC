def uppCons (frase):
    '''receb uma frase e retorna a mesma frase com todas as suas consoantes em maisculo e as demais letras exatamente como estavam'''
    '''str->str'''
    i=0
    a=0
    consoantes=''
    while i<len(frase):
        if frase[i] in 'aeiouAEIOUBCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            teste= str.upper(frase[i])
            teste2 = str.join ('A',' ')
            consoantes=consoantes+teste2
            
        i=i+1
    return consoantes