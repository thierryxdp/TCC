def uppCons(frase):
    '''retorna uma string com as consoantes que apareceram em um texto,
    maiusculas
    consoantes=consoantes+frase[i]
        i=i+1
        consoantes = ''
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':   
            consoantes = str.upper(consoantes) + frase[0:] 
    str->str'''
    
    vogais = ''
    x = 0
    while x < len(frase):  
        if frase[x] in 'aeiou':
            vogais = str.lower(vogais) + frase[x]    
        x = x + 1
    return  vogais