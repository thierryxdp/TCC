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
    i = 0
    while i < len(frase):  
        if frase[i] in 'aeiou':
            vogais = str.lower(vogais) + frase[1:]    
        i=i+1
    return  vogais