def uppCons(palavra):
    i=0
    consoantes=''
    while i<len(palavra):
        if palavra[i] in 'BCDFGHJKLMNPQRSTVWXYZ':
            consoantes = consoantes + consoantes[i]
        i=i+1
    return consoantes