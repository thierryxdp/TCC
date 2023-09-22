def uppCons (frase):
    '''receb uma frase e retorna a mesma frase com todas as suas consoantes em maisculo e as demais letras exatamente como estavam'''
    '''str->str'''
    i=0
    a=0
    consoantes=''
    while i<len(frase):
        if frase[i] in 'AEIOUBCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            teste= str.upper(frase[i])
            dois= str.replace (consoantes,frase[i],teste)
            consoantes=consoantes + frase[i]
            
        i=i+1
    return dois