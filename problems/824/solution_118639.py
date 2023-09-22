def uppCons(frase):
    '''retorna uma string com as consoantes que apareceram em um texto,
    maiusculas
    consoantes=consoantes+frase[i]
        i=i+1
    str->str'''
    consoantes = ''
    vogais = ''
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':   
            consoantes = str.upper(consoantes) + frase[i]   
        if frase[i] in 'AEIOUaeiou':
            vogais = str.lower(vogais) + frase[i]
            
        i=i+1
    return frase