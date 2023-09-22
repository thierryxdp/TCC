def uppCons(frase):
    """retorna a frase com as consoantes em maiúsculas"""
    i = 0 
    Nfrase = ''
    while i < len(frase):
        if frase[i] in 'AEIOUaeiou':
            Nfrase = Nfrase + frase[i]
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZÇbcdfghjklmnpqrstvwxyzç':
            Nfrase = Nfrase + str.upper(frase[i])
        if frase[i] not in 'AEIOUaeiouBCDFGHJKLMNPQRSTVWXYZÇbcdfghjklmnpqrstvwxyzç':
            Nfrase = Nfrase + frase[i]
        i = i + 1 
    return Nfrase